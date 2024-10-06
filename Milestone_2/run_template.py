#This is where the program will run from.

import wx
from template_frame import MyFrame1 as MyFrame
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import all_functions as af
import all_functions_ben as bf
# import winsound #helps me test whether the code reaches a point


class CurrFrame(MyFrame):
    def __init__(self):
        super().__init__(None)
        self.init_data = af.load_data("Food_Nutrition_Dataset.csv")
        # winsound.Beep(1000, 500) #testing noise
        self.pop_nut_select_grid()
        self.Layout()
        self.Show()

    # Populating the Nutrition Selection Grid, should be called during frame initialization.
    def pop_nut_select_grid(self):
        # Define column labels
        col_labels = ["Select", "Min", "Max", "Level"]
        for col, label in enumerate(col_labels):
            self.search_selection_grid.SetColLabelValue(col, label)

        # Get number of rows in the dataframe.
        rows = len(self.init_data)
        # Get the number of columns in the dataframe minus "food"
        columns = len(self.init_data.columns) - 1

        # Add rows to the grid based on the number of columns in the dataframe
        self.search_selection_grid.AppendRows(columns)

        # Set row labels using the names of the columns from the dataframe
        for row in range(columns):
            # Set row label using the column name, skipping "food"
            row_label = str(self.init_data.columns[row + 1])
            self.search_selection_grid.SetRowLabelValue(row, row_label)

            # Set checkbox in the first column
            self.search_selection_grid.SetCellRenderer(row, 0, wx.grid.GridCellBoolRenderer())  # Checkbox renderer
            self.search_selection_grid.SetCellEditor(row, 0, wx.grid.GridCellBoolEditor())  # Checkbox editor
            self.search_selection_grid.SetCellValue(row, 0, "0")  # Initially unchecked
            self.search_selection_grid.SetCellAlignment(row, 0, wx.ALIGN_CENTER, wx.ALIGN_CENTER)  # Center the checkbox

            # Set wxTextCtrl for columns 2 and 3 (Text inputs)
            for col in [1, 2]:
                self.search_selection_grid.SetCellEditor(row, col, wx.grid.GridCellTextEditor())  # Text editor
                if col == 1:
                    # Set "Min" column (index 1) to have initial value "0"
                    self.search_selection_grid.SetCellValue(row, col, "0")
                else:
                    # "Max" column will have an empty initial value
                    self.search_selection_grid.SetCellValue(row, col, "")

            # Set dropdown (wx.Choice) in the 4th column
            choice_editor = wx.grid.GridCellChoiceEditor(choices=["Low", "Mid", "High"])
            self.search_selection_grid.SetCellEditor(row, 3, choice_editor)
            self.search_selection_grid.SetCellValue(row, 3, "Mid")  # Default value

        # Auto resize columns to fit the contents
        self.search_selection_grid.AutoSizeColumns()
        # Set the row label size (width). Currently adjusted, change if needed.
        self.search_selection_grid.SetRowLabelSize(150)

    def on_nut_select_cell_click(self, event):
        row = event.GetRow()
        col = event.GetCol()

        if col == 0:  # Checkbox column
            current_value = self.search_selection_grid.GetCellValue(row, col)
            # Toggle the checkbox value
            new_value = "1" if current_value == "0" else "0"
            self.search_selection_grid.SetCellValue(row, col, new_value)
        elif col == 3:  # If the clicked cell is in the "Level" column (index 3)
            self.search_selection_grid.SetGridCursor(event.GetRow(), event.GetCol())
            self.search_selection_grid.EnableCellEditControl()  # Immediately enable the cell editor
        else:
            event.Skip()

    # Searching will use search_function followed by nutrition_range_filter or nutrition_level_filter
    def search_foods(self, event):
        # Get search term
        search_term = self.search_bar.GetValue().strip()
        # Perform initial search
        search_results, result_count = af.search_function(search_term, self.init_data)

        selected_nutrients = []

        for row in range(self.search_selection_grid.GetNumberRows()):
            nutrient = self.search_selection_grid.GetRowLabelValue(row)

            # Use the checkbox value to determine if the nutrient should be included
            if self.search_selection_grid.GetCellValue(row, 0) == '1':  # '1' means checked
                min_value = self.search_selection_grid.GetCellValue(row, 1)
                max_value = self.search_selection_grid.GetCellValue(row, 2)
                level = self.search_selection_grid.GetCellValue(row, 3)

                if min_value and max_value:
                    selected_nutrients.append({'nutrient': nutrient, 'min': float(min_value), 'max': float(max_value)})
                else: #level
                    selected_nutrients.append({'nutrient': nutrient, 'level': level})

        # Filtering results
        for filter in selected_nutrients:
            nutrient = filter['nutrient']
            if 'min' in filter and 'max' in filter:
                search_results = af.nutrition_range_filter(search_results, nutrient, filter['min'], filter['max'])
            elif 'level' in filter:
                search_results = af.nutrition_level_filter(search_results, nutrient, filter['level'])

        # Clear previous results
        self.search_results_list.ClearGrid()

        # Populate search_results_list grid
        for idx, (index, row) in enumerate(search_results.iterrows()):
            if idx >= self.search_results_list.GetNumberRows():
                self.search_results_list.AppendRows(1)  # Append a new row if necessary

            # Set the food name and other nutrient values
            self.search_results_list.SetCellValue(idx, 0, row['food'])
            self.search_results_list.SetCellValue(idx, 1, "Add")  # Column for "Add" action

        # Auto-size columns
        for col in range(0, self.search_results_list.GetNumberCols()):
            self.search_results_list.AutoSizeColumn(col)

        self.search_text.SetLabel(f"Results: {len(search_results)}")

    def add_food_to_grid(self, food_name):
        # Get the row corresponding to the selected food in init_data
        food_row = self.init_data[self.init_data['food'] == food_name]

        if not food_row.empty:
            # Get the number of rows in the target grid (selected food grid)
            current_row_count = self.selected_food_grid.GetNumberRows()

            # Add a new row for the selected food
            self.selected_food_grid.AppendRows(1)

            # Set the checkbox in the first column for the newly added row
            self.selected_food_grid.SetCellRenderer(current_row_count, 0, wx.grid.GridCellBoolRenderer())
            self.selected_food_grid.SetCellEditor(current_row_count, 0, wx.grid.GridCellBoolEditor())
            self.selected_food_grid.SetCellValue(current_row_count, 0, "0")  # Initially unchecked

            # Center the checkbox in the first column
            self.selected_food_grid.SetCellAlignment(current_row_count, 0, wx.ALIGN_CENTER, wx.ALIGN_CENTER)

            # Populate the new row with nutrient data from the dataframe
            for col in range(1, len(self.init_data.columns)):  # Start from 1 to skip the "food" column
                value = str(food_row.iloc[0, col])  # Get the nutrient value from the dataframe
                # Set value in the row index that was just added (current_row_count)
                self.selected_food_grid.SetCellValue(current_row_count, col, value)

            # Set the row label with the food name
            self.selected_food_grid.SetRowLabelValue(current_row_count, food_name)

            # Set column labels: first column is "Select", then dataframe column names
            self.selected_food_grid.SetColLabelValue(0, "Select")  # Checkbox column label
            for col in range(1, len(self.init_data.columns)):  # Start from 1 to skip the checkbox column
                self.selected_food_grid.SetColLabelValue(col,
                                                         self.init_data.columns[col])  # Column names from dataframe

            # Auto-size rows and columns after setting column labels
            for row in range(self.selected_food_grid.GetNumberRows()):
                self.selected_food_grid.AutoSizeRow(row)

            # Auto-size columns
            for col in range(0, self.selected_food_grid.GetNumberCols()):
                self.selected_food_grid.AutoSizeColumn(col)

    def on_result_select_cell_click(self, event):
        row = event.GetRow()
        col = event.GetCol()

        # If "Add" button (second column) is clicked
        if col == 1 and self.search_results_list.GetCellValue(row, col) == "Add":
            selected_food = self.search_results_list.GetCellValue(row, 0)  # Get the food name
            self.add_food_to_grid(selected_food)

        event.Skip()  # Skip the event to allow other default handling

    def bar_breakdown_plot(self, event): #not working
        checked_count = 0
        for row in range(self.selected_food_grid.GetNumberRows()):
            if self.selected_food_grid.GetCellValue(row, 0) == '1':  # '1' means checked:
                selected_food = self.selected_food_grid.GetRowLabelValue(row)
                checked_count += 1

        # Ensure exactly one checkbox is ticked
        if checked_count != 1:
            wx.MessageBox("Please check exactly one checkbox.", "Warning", wx.OK | wx.ICON_WARNING)
            return None  # Return None if the condition is not met

        # Locate the corresponding row in the DataFrame
        food_data = self.init_data[self.init_data['food'] == selected_food]

        if not food_data.empty:
            food_row = food_data.iloc[0]  # Get the first matching row
            af.nutrition_breakdown(food_row, 'Bar')


    # def pie_breakdown_plot(self, event): #not working
    #     af.nutrition_breakdown(, 'Pie')


    def remove_selected_food(self, event): #not working
        def remove_selected_rows(self, event):
            # List to store the indices of rows to be removed
            rows_to_remove = []

            # Iterate through the rows of the selected_food_grid
            for row in range(self.selected_food_grid.GetNumberRows()):
                if self.selected_food_grid.GetCellValue(row, 0) == '1':  # Check if the checkbox is checked
                    rows_to_remove.append(row)

            # Remove rows in reverse order to maintain index integrity
            for row in reversed(rows_to_remove):
                self.selected_food_grid.DeleteRows(row, 1)  # Delete the row

            # Optionally, you can display a message about the removal
            if rows_to_remove:
                wx.MessageBox(f"Removed {len(rows_to_remove)} row(s).", "Info", wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox("No rows selected for removal.", "Info", wx.OK | wx.ICON_INFORMATION)

    def onclickcompplot(self, event):
        event.Skip()
        food_inputs = [
                self.fw_f1_in.GetValue(),
                self.fw_f2_in.GetValue(),
                self.fw_f3_in.GetValue(),
                self.fw_f4_in.GetValue(),
                self.fw_f5_in.GetValue()
            ]
        nutrient = self.nutin_input.GetStringSelection()
        af.food_wars(food_inputs, nutrient, self.init_data)
        return 
    # Will use onclick event to plot using Ben's function.


if __name__ == "__main__":
    # Create a wx App instance
    app = wx.App()
    frame = CurrFrame()
    # Start the wx event loop
    app.MainLoop()