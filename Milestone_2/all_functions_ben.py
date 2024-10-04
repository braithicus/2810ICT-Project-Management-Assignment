
import wx
import wx.grid
import pandas as pd
import re
import matplotlib
matplotlib.use('WXAgg') # allows Matplotlib to render plots within wxPython.
# to embed a Matplotlib figure into a wxPanel in a wxPython application.
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt
import template_frame_ben
from template_frame import MyFrame1 as MyFrame


def load_data(filepath):
  try:
    return pd.read_csv(filepath)
  except FileNotFoundError as e:
    raise FileNotFoundError(f"Error: File Not Found. {e}") from e
  
import pandas as pd
import matplotlib.pyplot as plt

def food_wars(food_inputs, nutrient, df):
    # Filter out empty inputs and ensure at least two foods are provided
    food_inputs = [food for food in food_inputs if food]
    if len(food_inputs) < 2:
        raise ValueError("Please enter at least two foods to compare.")
    
    # Filter data for selected foods and nutrient
    df_filtered = df[df['food'].isin(food_inputs)]
    if nutrient not in df.columns:
        raise ValueError(f"Nutrient '{nutrient}' not found in data.")

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.bar(df_filtered['food'], df_filtered[nutrient], color='skyblue')
    plt.xlabel('Food')
    plt.ylabel(nutrient)
    plt.title(f'Food Wars: The {nutrient} Battles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return df_filtered

""""
EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

#Does the shit 
#Replaced all the times it would read or use the csv with filepath instead of the csv itself.
#Change if needed but this is just generic and designed to work with with template_frame_ben.py
#Also it brings up Food Wars page first. I dont care to fix it right now, like the saying says "If it ain't broke, don't touch it!"
class MyMainFrame(MyFrame):
    def __init__(self, parent=None, *args, **kw):
        super(MyMainFrame, self).__init__(parent, *args, **kw)
        self.df = pd.read_csv(filepath)
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership = True)
        self.m_grid1.AutoSize()
        self.Show(True)
        self.Layout()

    def onclickcompplot(self, event):
        # Get input values from the template frame
        food_inputs = [
            self.fw_f1_in.GetValue(),
            self.fw_f2_in.GetValue(),
            self.fw_f3_in.GetValue(),
            self.fw_f4_in.GetValue(),
            self.fw_f5_in.GetValue()
        ]
        nutrient = self.nutin_input.GetValue()

        # Filter out empty inputs and ensure at least two foods are provided
        food_inputs = [food for food in food_inputs if food]
        if len(food_inputs) < 2:
            wx.MessageBox("Please enter at least two foods to compare.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Load data from CSV (adjust the file path as needed)
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:
            wx.MessageBox("The data file could not be found.", "Error", wx.OK | wx.ICON_ERROR)
            return 

        # Filter data for selected foods and nutrient
        df_filtered = df[df['food'].isin(food_inputs)]
        if nutrient not in df.columns:
            wx.MessageBox(f"Nutrient '{nutrient}' not found in data.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Plotting the data
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(df_filtered['food'], df_filtered[nutrient], color='skyblue')
            plt.xlabel('Food')
            plt.ylabel(nutrient)
            plt.title(f'Comparison of {nutrient} for Selected Foods')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            wx.MessageBox(f"An error occurred while plotting: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
            
        # Overload your event function
    def search_tabfood_input(self, event):
      event.Skip()
      keyword1 = self.searchfood_input.GetValue()
      pattern = f".*{re.escape(keyword1)}.*"
      ser_food = self.df["food"]
      index = ser_food.str.contains(pattern, case=False, regex=True)
      df_filtered = self.df[index]
      self.m_grid1.ClearGrid()
      self.table = DataTable(df_filtered)
      self.m_grid1.SetTable(self.table, takeOwnership = True)
      self.m_grid1.AutoSize()
      text = f"The number of Results: {len(df_filtered)}"
      self.m_staticText3.SetLabel(text)



class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data


    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr



if __name__ == "__main__":
    app = wx.App(False)
    frame = MyMainFrame()
    frame.Show()
    app.MainLoop() """



class MyMainFrame(MyFrame):
    def __init__(self, parent=None, *args, **kw):
        super(MyMainFrame, self).__init__(parent, *args, **kw)
        self.df = pd.read_csv("sample_data.csv")
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership = True)
        self.m_grid1.AutoSize()
        self.Show(True)
        self.Layout()
    #getting inputs for food wars 
    def onclickcompplot(self, event):
        # Get input values from the template frame
        food_inputs = [
            self.fw_f1_in.GetValue(),
            self.fw_f2_in.GetValue(),
            self.fw_f3_in.GetValue(),
            self.fw_f4_in.GetValue(),
            self.fw_f5_in.GetValue()
        ]
        nutrient = self.nutin_input.GetValue()

        # Filter out empty inputs and ensure at least two foods are provided
        food_inputs = [food for food in food_inputs if food]
        if len(food_inputs) < 2:
            wx.MessageBox("Please enter at least two foods to compare.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Load sample data from CSV (adjust the file path as needed)
        try:
            df = pd.read_csv("sample_data.csv")
        except FileNotFoundError:
            wx.MessageBox("The data file could not be found.", "Error", wx.OK | wx.ICON_ERROR)
            return 

        # Filter data for selected foods and nutrient
        df_filtered = df[df['food'].isin(food_inputs)]
        if nutrient not in df.columns:
            wx.MessageBox(f"Nutrient '{nutrient}' not found in data.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Plotting the data
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(df_filtered['food'], df_filtered[nutrient], color='skyblue')
            plt.xlabel('Food')
            plt.ylabel(nutrient)
            plt.title(f'Food Wars: The {nutrient} Battles')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            wx.MessageBox(f"An error occurred while plotting: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)
            
        # Overload your event function
    def search_tabfood_input(self, event):
      event.Skip()
      keyword1 = self.searchfood_input.GetValue()
      pattern = f".*{re.escape(keyword1)}.*"
      ser_food = self.df["food"]
      index = ser_food.str.contains(pattern, case=False, regex=True)
      df_filtered = self.df[index]
      self.m_grid1.ClearGrid()
      self.table = DataTable(df_filtered)
      self.m_grid1.SetTable(self.table, takeOwnership = True)
      self.m_grid1.AutoSize()
      text = f"The number of Results: {len(df_filtered)}"
      self.m_staticText3.SetLabel(text)


    def onclicklvlfil(self, event):
        event.Skip()
        
        # Get level and nutrient choices from the dropdown menus
        level = self.m_choice2.GetStringSelection()
        nutrient = self.m_choice3.GetStringSelection()
        
        # Verify if a valid nutrient is selected
        if nutrient not in self.df.columns:
            wx.MessageBox(f"Nutrient '{nutrient}' not found in data.", "Error", wx.OK | wx.ICON_ERROR)
            return
        
        # Calculate thresholds for low, mid, and high levels
        max_value = self.df[nutrient].max()
        low_threshold = max_value * 0.33
        mid_threshold = max_value * 0.66

        # Apply the filter based on the selected level
        if level == "Low":
            df_filtered = self.df[self.df[nutrient] < low_threshold]
        elif level == "Mid":
            df_filtered = self.df[(self.df[nutrient] >= low_threshold) & (self.df[nutrient] <= mid_threshold)]
        elif level == "High":
            df_filtered = self.df[self.df[nutrient] > mid_threshold]
        else:
            wx.MessageBox(f"Invalid level '{level}' selected.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Sort the filtered data in descending order by the selected nutrient
        df_filtered = df_filtered.sort_values(by=nutrient, ascending=False)

        # Update the grid with the filtered data
        self.m_grid1.ClearGrid()
        self.table = DataTable(df_filtered)
        self.m_grid1.SetTable(self.table, takeOwnership=True)
        self.m_grid1.AutoSize()
        
        # Update the label to show the number of results
        text = f"The number of Results: {len(df_filtered)}"
        self.m_staticText3.SetLabel(text)

class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data


    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyMainFrame()
    frame.Show()
    app.MainLoop()