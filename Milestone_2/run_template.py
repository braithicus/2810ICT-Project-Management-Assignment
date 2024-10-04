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
        self.Show()

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