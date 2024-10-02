import all_functions_ben as af
import pandas as pd
import pytest
import wx.grid
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


## Testing Code
class MyMainFrame(MyFrame):
    def __init__(self, parent=None, *args, **kw):
        super(MyMainFrame, self).__init__(parent, *args, **kw)


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

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyMainFrame()
    frame.Show()
    app.MainLoop()


## End Testing Code

""" class DataTable(wx.grid.GridTableBase):
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

class MyMainFrame(MyFrame):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.Layout()
        self.Show(True)

    def onclickcompplot( self, event ):
        event.Skip()
        categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
        sizes = [10, 10, 10, 10]
        colours = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] # must use these colours
        fig = self.plot_data(categories, sizes, colours)
        h, w = self.m_panel1.GetSize()
        fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())
        canvas = FigureCanvasWxAgg(self.m_panel1, -1, fig)
        canvas.SetSize((h, w))
        self.Layout()

    def plot_data(self, categories, sizes, colours):
        fig, axes = plt.subplots(1, 1, figsize=(12, 6)) # adding multiple subplots
        ax1 = axes
        ax1.pie(sizes, labels=categories, autopct = '%1.1f%%', colors=colours, shadow=True, explode=(0.1, 0, 0, 0))
        ax1.set_title("Pie chart")
        return fig

#Search function
#Change the Regex filter i.e. keyword1 and keyword2
class CalcFrame(MyFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.df = pd.read_csv("sample_data.csv")
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership = True)
        self.m_grid1.AutoSize()
        self.Show(True)
        self.Layout()
        
    # Overload your event function
    def search_tabfood_input(self, event):
        event.Skip()

        keyword1 = self.m_textCtrl3.GetValue()
        keyword2 = self.m_textCtrl4.GetValue()

        
        pattern = f"^({keyword1}|{keyword2}|([{keyword1[0]}-{keyword2[0]}][0-9]*(\\.[0-9]*)?))"

        ser_price = self.df["price"]
        index = []
        for price in ser_price:
            if re.search(pattern, str(price)):
                index.append(True)
            else:
                index.append(False)

        df_filtered = self.df[index]
        self.m_grid1.ClearGrid()

        self.table = DataTable(df_filtered)
        self.m_grid1.SetTable(self.table, takeOwnership = True)
        self.m_grid1.AutoSize()
        text = f"The number of rows: {len(df_filtered)}"
        self.m_staticText1.SetLabel(text)


if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop() """