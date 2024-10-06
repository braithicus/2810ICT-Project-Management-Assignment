import all_functions_ben as af
import pandas as pd
import pytest
import wx.grid
import re
import template_frame_ben
from template_frame_ben import MyFrame1 as MyFrame
import matplotlib
matplotlib.use('WXAgg') # allows Matplotlib to render plots within wxPython.
# to embed a Matplotlib figure into a wxPanel in a wxPython application.
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

# calling the load data function on a csv with the same data as the test dataframe
# this small test dataframe is used globally throughout most tests
df = af.load_data('sample_data.csv')
EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

def test_load_data_valid():
  # making a small dataframe for testing
  test_data = pd.DataFrame({
  'food': ["Peanut Butter", "Apple Pie", "Another Random Item", "Butter Scotch"],
  'Poison': [345, 987, 531, 7],
  'Row Number': [1, 2, 3, 4]
  })


  # assert that the function returns the same result as the test dataframe
  pd.testing.assert_frame_equal(df, test_data)


def test_load_data_invalid():
  # assert the fail returns file not found error
  with pytest.raises(FileNotFoundError):   
    af.load_data('non-existent-file.csv')


## Works
class MyMainFrame(MyFrame):
    def __init__(self, parent=None, *args, **kw):
        super(MyMainFrame, self).__init__(parent, *args, **kw)
        self.df = pd.read_csv("sample_data.csv")
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