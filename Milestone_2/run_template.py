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


# Should probably put Ben's functions into all_functions.py before they get imported.
# I completely forget where or what nutin_input is used for.
# nutin_input is the choice of nutrition in food wars
df = pd.read_csv("Food_Nutrition_Dataset.csv")
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
            choice_editor = wx.grid.GridCellChoiceEditor(choices=["Low", "Medium", "High"])
            self.search_selection_grid.SetCellEditor(row, 3, choice_editor)
            self.search_selection_grid.SetCellValue(row, 3, "Medium")  # Default value

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
        elif col == 3: # If the clicked cell is in the "Level" column (index 3)
            self.search_selection_grid.SetGridCursor(event.GetRow(), event.GetCol())
            self.search_selection_grid.EnableCellEditControl()  # Immediately enable the cell editor
        else:
            # Allow normal behavior for other cells
            event.Skip()

    # Searching will use search_function followed by nutrition_range_filter or nutrition_level_filter
    def search_foods(self, event):
        # clear currently printed search results
        search_term = self.search_bar.GetValue()
        dataf, result_count = af.search_function(search_term, self.init_data)
        # The following needs to occur before the search
        # iterate through grid rows
        #     if checkbox is ticked:
        #         if (min cell == 0) and (max cell empty):
        #             add necessary level information to search
        #         else:
        #             add necessary range information to search
        # result_count -= 1

        # Clear existing results in the grid
        self.search_results_list.ClearGrid()

        # Ensure the grid has enough rows to display all search results
        current_rows = self.search_results_list.GetNumberRows()
        if current_rows < result_count:
            self.search_results_list.AppendRows(result_count - current_rows)
        elif current_rows > result_count:
            self.search_results_list.DeleteRows(0, current_rows - result_count)

        # Populate the grid with search results
        for row in range(result_count):
            food_name = dataf.iloc[row, 0]  # Get the food name from the dataframe
            self.search_results_list.SetCellValue(row, 0, food_name)

            # Set the second column with the label "Add" (acting as a button)
            self.search_results_list.SetCellValue(row, 1, "Add")

        # Auto-resize the columns
        self.search_results_list.AutoSizeColumns()

    def add_food_to_grid(self, food_name):
        # Get the row corresponding to the selected food in init_data
        food_row = self.init_data[self.init_data['food'] == food_name]

        if not food_row.empty:
            # Get the number of rows in the target grid (selected food grid)
            current_row_count = self.selected_food_grid.GetNumberRows()

            # Add a new row for the selected food
            self.selected_food_grid.AppendRows(1)

            # Populate the new row with nutrient data from the dataframe
            for col in range(1, len(self.init_data.columns)):  # Start from 1 to skip the "food" column
                value = str(food_row.iloc[0, col])
                # Set value in the row index that was just added (current_row_count)
                self.selected_food_grid.SetCellValue(current_row_count, col - 1, value)

            # Add a checkbox in the first column for the newly added row
            self.selected_food_grid.SetCellRenderer(current_row_count, 0, wx.grid.GridCellBoolRenderer())
            self.selected_food_grid.SetCellEditor(current_row_count, 0, wx.grid.GridCellBoolEditor())
            self.selected_food_grid.SetCellValue(current_row_count, 0, "0")  # Initially unchecked

    def on_result_select_cell_click(self, event):
        row = event.GetRow()
        col = event.GetCol()

        # If "Add" button (second column) is clicked
        if col == 1 and self.search_results_list.GetCellValue(row, col) == "Add":
            selected_food = self.search_results_list.GetCellValue(row, 0)  # Get the food name
            self.add_food_to_grid(selected_food)

        event.Skip()  # Skip the event to allow other default handling

    # I've written the fill_food_wars to store the values for the foods and the nutirients, this does not plot anything and just stores them, feel free to change it but this should work currently
    def fill_food_wars(self, event):
        #food_inputs = [
                #self.fw_f1_in.GetValue(),
                #self.fw_f2_in.GetValue(),
                #self.fw_f3_in.GetValue(),
                #self.fw_f4_in.GetValue(),
                #self.fw_f5_in.GetValue()
            #]
        #nutrient = self.nutin_input.GetSelection()

        # Filter out empty inputs and ensure at least two foods are provided
        #selection_list = [food for food in food_inputs if food]
        
        #if len(selection_list) > 5:
            "You can only select a maximum of 5 foods for Food Wars"
        #elif len(selection_list) < 2:
            "You need to select at least 2 foods for Food Wars"
        #else:
        #selection_list = bf.fill_food_wars()
    #     else:
    #         iterate and fill fw_f1_in, fw_f2_in, fw_f3_in, etc with selection_list or dataframe or whatever

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
        bf.food_wars(food_inputs, nutrient, df)
        return 
    # Will use onclick event to plot using Ben's function.

    # def update_breakdown(self, event):
    #     grab selected values from grid
    #     if one value is selected:
    #         af.nutrition_breakdown(foodRow=)
    #     elif > one value is selected:
    #         popup saying "You can only select one food for Nutrition Breakdown"
    #     else: # no value
    #         popup saying "You need to select at least one food for Nutrition Breakdown"


if __name__ == "__main__":
    # Create a wx App instance
    app = wx.App()
    frame = CurrFrame()
    # Start the wx event loop
    app.MainLoop()