# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"ST Group"), pos = wx.DefaultPosition, size = wx.Size( 800,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.table_page = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel6 = wx.Panel( self.table_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText19 = wx.StaticText( self.m_panel6, wx.ID_ANY, _(u"Enter Food"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText19.Wrap( -1 )

        bSizer9.Add( self.m_staticText19, 0, wx.ALL, 5 )

        self.searchfood_input = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        bSizer9.Add( self.searchfood_input, 1, wx.ALL, 5 )

        self.search_butt = wx.Button( self.m_panel6, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.search_butt, 0, wx.ALL, 5 )


        bSizer5.Add( bSizer9, 0, wx.EXPAND, 5 )

        bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self.m_panel6, wx.ID_ANY, _(u"Searched:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer61.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.search_input_text = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_input_text.Wrap( -1 )

        bSizer61.Add( self.search_input_text, 1, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self.m_panel6, wx.ID_ANY, _(u"Number of Results:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer61.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.num_results = wx.StaticText( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.num_results.Wrap( -1 )

        bSizer61.Add( self.num_results, 1, wx.ALL, 5 )


        bSizer5.Add( bSizer61, 0, wx.EXPAND, 5 )

        self.m_panel71 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText14 = wx.StaticText( self.m_panel71, wx.ID_ANY, _(u"Level Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        bSizer14.Add( self.m_staticText14, 0, wx.ALL, 5 )

        m_choice2Choices = [ _(u"Low"), _(u"Mid"), _(u"High") ]
        self.m_choice2 = wx.Choice( self.m_panel71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        bSizer14.Add( self.m_choice2, 0, wx.ALL, 5 )

        self.m_staticText15 = wx.StaticText( self.m_panel71, wx.ID_ANY, _(u"Nutrition"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        bSizer14.Add( self.m_staticText15, 0, wx.ALL, 5 )

        m_choice3Choices = [ _(u"Poison"), _(u"Caloric Value"), _(u"Fat"), _(u"Saturated Fats"), _(u"Monounsaturated Fats"), _(u"Polyunsaturated Fats"), _(u"Carbohydrates"), _(u"Sugars"), _(u"Protein"), _(u"Dietary Fiber"), _(u"Cholesterol"), _(u"Sodium"), _(u"Water"), _(u"Vitamin A"), _(u"Vitamin B1"), _(u"Vitamin B11"), _(u"Vitamin B12"), _(u"Vitamin B2"), _(u"Vitamin B3"), _(u"Vitamin B5"), _(u"Vitamin B6"), _(u"Vitamin C"), _(u"Vitamin D"), _(u"Vitamin E"), _(u"Vitamin K"), _(u"Calcium"), _(u"Copper"), _(u"Iron"), _(u"Magnesium"), _(u"Manganese"), _(u"Phosphorus"), _(u"Potassium"), _(u"Selenium"), _(u"Zinc"), _(u"Nutrition Density") ]
        self.m_choice3 = wx.Choice( self.m_panel71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        bSizer14.Add( self.m_choice3, 0, wx.ALL, 5 )

        self.Level_Filter = wx.Button( self.m_panel71, wx.ID_ANY, _(u"Level Filter"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.Level_Filter, 0, wx.ALL, 5 )


        self.m_panel71.SetSizer( bSizer14 )
        self.m_panel71.Layout()
        bSizer14.Fit( self.m_panel71 )
        bSizer5.Add( self.m_panel71, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_grid1 = wx.grid.Grid( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 5, 5 )
        self.m_grid1.EnableEditing( False )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.AutoSizeColumns()
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.AutoSizeRows()
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer5.Add( self.m_grid1, 0, wx.ALL, 5 )


        self.m_panel6.SetSizer( bSizer5 )
        self.m_panel6.Layout()
        bSizer5.Fit( self.m_panel6 )
        bSizer8.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )


        self.table_page.SetSizer( bSizer7 )
        self.table_page.Layout()
        bSizer7.Fit( self.table_page )
        self.m_notebook1.AddPage( self.table_page, _(u"le table"), True )
        self.fw_page = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer71 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self.fw_page, wx.ID_ANY, _(u"Food Wars"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer71.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText18 = wx.StaticText( self.fw_page, wx.ID_ANY, _(u"Enter up to 5 foods (minimum 2) and compare them against each other on a bar graph"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer71.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_panel81 = wx.Panel( self.fw_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText65 = wx.StaticText( self.m_panel81, wx.ID_ANY, _(u"Enter food 1 here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText65.Wrap( -1 )

        bSizer91.Add( self.m_staticText65, 0, wx.ALL, 5 )

        self.fw_f1_in = wx.TextCtrl( self.m_panel81, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        bSizer91.Add( self.fw_f1_in, 1, wx.ALL, 5 )


        self.m_panel81.SetSizer( bSizer91 )
        self.m_panel81.Layout()
        bSizer91.Fit( self.m_panel81 )
        bSizer71.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel9 = wx.Panel( self.fw_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer911 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText64 = wx.StaticText( self.m_panel9, wx.ID_ANY, _(u"Enter food 2 here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText64.Wrap( -1 )

        bSizer911.Add( self.m_staticText64, 0, wx.ALL, 5 )

        self.fw_f2_in = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        bSizer911.Add( self.fw_f2_in, 1, wx.ALL, 5 )


        self.m_panel9.SetSizer( bSizer911 )
        self.m_panel9.Layout()
        bSizer911.Fit( self.m_panel9 )
        bSizer71.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel10 = wx.Panel( self.fw_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer912 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText63 = wx.StaticText( self.m_panel10, wx.ID_ANY, _(u"Enter food 3 here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText63.Wrap( -1 )

        bSizer912.Add( self.m_staticText63, 0, wx.ALL, 5 )

        self.fw_f3_in = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        bSizer912.Add( self.fw_f3_in, 1, wx.ALL, 5 )


        self.m_panel10.SetSizer( bSizer912 )
        self.m_panel10.Layout()
        bSizer912.Fit( self.m_panel10 )
        bSizer71.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel11 = wx.Panel( self.fw_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer913 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText62 = wx.StaticText( self.m_panel11, wx.ID_ANY, _(u"Enter food 4 here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText62.Wrap( -1 )

        bSizer913.Add( self.m_staticText62, 0, wx.ALL, 5 )

        self.fw_f4_in = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        bSizer913.Add( self.fw_f4_in, 1, wx.ALL, 5 )


        self.m_panel11.SetSizer( bSizer913 )
        self.m_panel11.Layout()
        bSizer913.Fit( self.m_panel11 )
        bSizer71.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel12 = wx.Panel( self.fw_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer914 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText61 = wx.StaticText( self.m_panel12, wx.ID_ANY, _(u"Enter food 5 here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText61.Wrap( -1 )

        bSizer914.Add( self.m_staticText61, 0, wx.ALL, 5 )

        self.fw_f5_in = wx.TextCtrl( self.m_panel12, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        bSizer914.Add( self.fw_f5_in, 1, wx.ALL, 5 )


        self.m_panel12.SetSizer( bSizer914 )
        self.m_panel12.Layout()
        bSizer914.Fit( self.m_panel12 )
        bSizer71.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel13 = wx.Panel( self.fw_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.m_panel13, wx.ID_ANY, _(u"Enter Nutrition here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText6.Wrap( -1 )

        bSizer20.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.nutin_input = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
        bSizer20.Add( self.nutin_input, 1, wx.ALL, 5 )


        self.m_panel13.SetSizer( bSizer20 )
        self.m_panel13.Layout()
        bSizer20.Fit( self.m_panel13 )
        bSizer71.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )

        self.fw_compare_button = wx.Button( self.fw_page, wx.ID_ANY, _(u"Compare"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer71.Add( self.fw_compare_button, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        self.fw_page.SetSizer( bSizer71 )
        self.fw_page.Layout()
        bSizer71.Fit( self.fw_page )
        self.m_notebook1.AddPage( self.fw_page, _(u"Food Wars"), False )

        bSizer6.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.search_butt.Bind( wx.EVT_BUTTON, self.search_tabfood_input )
        self.Level_Filter.Bind( wx.EVT_BUTTON, self.onclicklvlfil )
        self.fw_compare_button.Bind( wx.EVT_BUTTON, self.onclickcompplot )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def search_tabfood_input( self, event ):
        event.Skip()

    def onclicklvlfil( self, event ):
        event.Skip()

    def onclickcompplot( self, event ):
        event.Skip()


