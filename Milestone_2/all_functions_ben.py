
import wx
import wx.grid
import pandas as pd
import re

from template_frame import MyFrame1 as MyFrame1

def load_data(filepath):
  try:
    return pd.read_csv(filepath)
  except FileNotFoundError as e:
    raise FileNotFoundError(f"Error: File Not Found. {e}") from e




EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'


#Creates table and cha
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


#Search function
#Change the Regex filter i.e. keyword1 and keyword2
class CalcFrame(MyFrame1):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.df = pd.read_csv("sample_data.csv")
        self.table = DataTable(self.df)
        self.m_grid1.SetTable(self.table, takeOwnership = True)
        self.m_grid1.AutoSize()
        self.Show(True)
        self.Layout()
        
    # Overload your event function
    def OnSearch(self, event):
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
    app.MainLoop()