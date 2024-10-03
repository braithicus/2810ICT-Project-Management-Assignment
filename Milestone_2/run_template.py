#This is where the program will run from.

import wx
from template_frame import MyFrame1 as MyFrame
import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import all_functions as af
import all_functions_ben as bf

# Should probably put Ben's functions into all_functions.py before they get imported.
# I completely forget where or what nutin_input is used for.

class MyApp(wx.App):
    def OnInit(self):
        # Create an instance of the frame (the main window)
        data = af.load_data("Food_Nutrition_Dataset.csv")
        frame = MyFrame(None)

        # Show the frame
        frame.Show(True)

        return True

    # Searching will use Billy's search_function followed by nutrition_range_filter or nutrition_level_filter
    # def food_search(self, event):
    #     search_term = .get from search_bar
    #     dframeloc, result_count = af.search_function(search_term, data)
    #     if using range:
    #         for item in dframeloc:
    #             dframeloc = nutrition_range_filter(dframeloc, item, min_check_val, max_check_val)
    #     elif using level:
    #         for item in dframeloc:
    #             dframeloc = nutrition_level_filter(dframeloc, item, level)

    # def food_wars_plot(self, event):
    #     food_wars = bf.onclickcompplot()
    #     return food_wars
    # Will use onclick event to plot using Ben's function.
    #

if __name__ == "__main__":
    # Create a wx App instance
    app = MyApp(False)

    # Start the wx event loop
    app.MainLoop()
