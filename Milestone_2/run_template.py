#This is where the program will run from.

import wx
from template_frame import MyFrame1 as MyFrame
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import all_functions as af
import all_functions_ben as bf
import winsound #helps me test whether the code reaches a point

# Should probably put Ben's functions into all_functions.py before they get imported.
# I completely forget where or what nutin_input is used for.

class CurrFrame(MyFrame):
    def __init__(self):
        super().__init__(None)
        self.init_data = af.load_data("Food_Nutrition_Dataset.csv")
        winsound.Beep(1000, 500) #testing noise
        self.pop_nut_select_grid()
        self.Show()

    # Populating the Nutrition Selection Grid, should be called during frame initialization.
    def pop_nut_select_grid(self):
        # Define column labels
        col_labels = ["Select", "Min", "Max", "Level"]
        for col, label in enumerate(col_labels):
            self.search_selection_grid.SetColLabelValue(col, label)

        rows = len(self.init_data)
        # Add rows to the grid based on the dataframe length
        self.search_selection_grid.AppendRows(rows)

        for row in range(rows):
            # Set checkbox in the first column
            self.search_selection_grid.SetCellRenderer(row, 0, wx.grid.GridCellBoolRenderer())  # Checkbox renderer
            self.search_selection_grid.SetCellEditor(row, 0, wx.grid.GridCellBoolEditor())  # Checkbox editor
            self.search_selection_grid.SetCellValue(row, 0, "0")  # Initially unchecked
            # Center the checkboxes horizontally and vertically
            self.search_selection_grid.SetCellAlignment(row, 0, wx.ALIGN_CENTER, wx.ALIGN_CENTER)

            # Populate other columns with dataframe data
            for col in range(1, self.search_selection_grid.GetNumberCols()):
                value = str(self.init_data.iloc[row, col - 1])
                self.search_selection_grid.SetCellValue(row, col, value)

        # Auto resize columns to fit the contents
        self.search_selection_grid.AutoSizeColumns()

    # Searching will use search_function followed by nutrition_range_filter or nutrition_level_filter
    def search_foods(self, event):
        winsound.Beep(1000, 500)
        search_term = self.search_bar.GetValue()
        winsound.Beep(1000, 500)
        dataf, result_count = af.search_function(search_term, self.init_data)
        if search_term:
            print(f"Current DataFrame:\n {dataf}")
        # if using range:
        #     for item in dataf:
        #         dataf = nutrition_range_filter(dataf, item, min_check_val, max_check_val)

        # elif using level:
        #     for item in dataf:
        #         dataf = nutrition_level_filter(dataf, item, level)

    # def food_wars_plot(self, event):
    #     food_wars = bf.onclickcompplot()
    #     return food_wars
    # Will use onclick event to plot using Ben's function.
    #

if __name__ == "__main__":
    # Create a wx App instance
    app = wx.App()
    frame = CurrFrame()
    # Start the wx event loop
    app.MainLoop()