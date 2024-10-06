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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Food Comparison GUI"), pos = wx.DefaultPosition, size = wx.Size( 890,548 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.gui_panel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.VERTICAL )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        gbSizer1.SetMinSize( wx.Size( 1,1 ) )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

        self.search_bar = wx.TextCtrl( self.gui_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.search_bar, 3, wx.ALL, 5 )

        self.search_button = wx.Button( self.gui_panel, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer16.Add( self.search_button, 1, wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 5 )


        bSizer12.Add( bSizer16, 0, wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.VERTICAL )

        self.search_text = wx.StaticText( self.gui_panel, wx.ID_ANY, _(u"Search Results:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_text.Wrap( -1 )

        bSizer17.Add( self.search_text, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.search_results_list = wx.grid.Grid( self.gui_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.search_results_list.CreateGrid( 0, 2 )
        self.search_results_list.EnableEditing( True )
        self.search_results_list.EnableGridLines( True )
        self.search_results_list.EnableDragGridSize( False )
        self.search_results_list.SetMargins( 0, 0 )

        # Columns
        self.search_results_list.SetColSize( 0, 20 )
        self.search_results_list.SetColSize( 1, 18 )
        self.search_results_list.AutoSizeColumns()
        self.search_results_list.EnableDragColMove( False )
        self.search_results_list.EnableDragColSize( True )
        self.search_results_list.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.search_results_list.AutoSizeRows()
        self.search_results_list.EnableDragRowSize( True )
        self.search_results_list.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.search_results_list.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer17.Add( self.search_results_list, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer12.Add( bSizer17, 1, wx.EXPAND, 5 )


        gbSizer1.Add( bSizer12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        self.search_selection_grid = wx.grid.Grid( self.gui_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.search_selection_grid.CreateGrid( 0, 4 )
        self.search_selection_grid.EnableEditing( True )
        self.search_selection_grid.EnableGridLines( True )
        self.search_selection_grid.EnableDragGridSize( False )
        self.search_selection_grid.SetMargins( 0, 0 )

        # Columns
        self.search_selection_grid.AutoSizeColumns()
        self.search_selection_grid.EnableDragColMove( False )
        self.search_selection_grid.EnableDragColSize( True )
        self.search_selection_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.search_selection_grid.AutoSizeRows()
        self.search_selection_grid.EnableDragRowSize( True )
        self.search_selection_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.search_selection_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer13.Add( self.search_selection_grid, 1, wx.ALL|wx.EXPAND, 5 )


        gbSizer1.Add( bSizer13, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.gui_panel, wx.ID_ANY, _(u"Selected Foods") ), wx.VERTICAL )

        bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

        self.export_table_button = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Export Table"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.export_table_button, 0, wx.ALL, 5 )

        self.breakdown_button = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Update Breakdown"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.breakdown_button, 0, wx.ALL, 5 )

        self.food_wars_button = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Fill Food Wars"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.food_wars_button, 0, wx.ALL, 5 )

        self.remove_button = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Remove Selected"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer18.Add( self.remove_button, 0, wx.ALL, 5 )


        sbSizer2.Add( bSizer18, 0, wx.EXPAND, 5 )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        self.selected_food_grid = wx.grid.Grid( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.selected_food_grid.CreateGrid( 1, 36 )
        self.selected_food_grid.EnableEditing( True )
        self.selected_food_grid.EnableGridLines( True )
        self.selected_food_grid.EnableDragGridSize( False )
        self.selected_food_grid.SetMargins( 0, 0 )

        # Columns
        self.selected_food_grid.AutoSizeColumns()
        self.selected_food_grid.EnableDragColMove( False )
        self.selected_food_grid.EnableDragColSize( True )
        self.selected_food_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.selected_food_grid.AutoSizeRows()
        self.selected_food_grid.EnableDragRowSize( True )
        self.selected_food_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.selected_food_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer19.Add( self.selected_food_grid, 1, wx.ALL|wx.EXPAND, 5 )


        sbSizer2.Add( bSizer19, 1, wx.EXPAND, 5 )


        gbSizer1.Add( sbSizer2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND, 5 )


        gbSizer1.AddGrowableCol( 0 )
        gbSizer1.AddGrowableCol( 1 )
        gbSizer1.AddGrowableRow( 0 )
        gbSizer1.AddGrowableRow( 1 )

        self.gui_panel.SetSizer( gbSizer1 )
        self.gui_panel.Layout()
        gbSizer1.Fit( self.gui_panel )
        self.m_notebook1.AddPage( self.gui_panel, _(u"GUI"), True )
        self.breakdown_panel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )


        self.breakdown_panel.SetSizer( bSizer22 )
        self.breakdown_panel.Layout()
        bSizer22.Fit( self.breakdown_panel )
        self.m_notebook1.AddPage( self.breakdown_panel, _(u"Breakdown"), False )
        self.food_wars_panel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.food_wars_title = wx.StaticText( self.food_wars_panel, wx.ID_ANY, _(u"Food Wars"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.food_wars_title.Wrap( -1 )

        bSizer11.Add( self.food_wars_title, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.food_wars_explain = wx.StaticText( self.food_wars_panel, wx.ID_ANY, _(u"Enter up to 5 foods (minimum 2) and compare them against each other on a bar graph"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.food_wars_explain.Wrap( -1 )

        bSizer11.Add( self.food_wars_explain, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        bSizer121 = wx.BoxSizer( wx.VERTICAL )

        bSizer131 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( self.food_wars_panel, wx.ID_ANY, _(u"Enter Food 1 Here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText5.Wrap( -1 )

        bSizer131.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.fw_f1_in = wx.TextCtrl( self.food_wars_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131.Add( self.fw_f1_in, 1, wx.ALL, 5 )


        bSizer121.Add( bSizer131, 1, wx.EXPAND, 5 )

        bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.food_wars_panel, wx.ID_ANY, _(u"Enter Food 2 Here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText6.Wrap( -1 )

        bSizer141.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.fw_f2_in = wx.TextCtrl( self.food_wars_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer141.Add( self.fw_f2_in, 1, wx.ALL, 5 )


        bSizer121.Add( bSizer141, 1, wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self.food_wars_panel, wx.ID_ANY, _(u"Enter Food 3 Here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText7.Wrap( -1 )

        bSizer15.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.fw_f3_in = wx.TextCtrl( self.food_wars_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.fw_f3_in, 1, wx.ALL, 5 )


        bSizer121.Add( bSizer15, 1, wx.EXPAND, 5 )

        bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self.food_wars_panel, wx.ID_ANY, _(u"Enter Food 4 Here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText8.Wrap( -1 )

        bSizer181.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.fw_f4_in = wx.TextCtrl( self.food_wars_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer181.Add( self.fw_f4_in, 1, wx.ALL, 5 )


        bSizer121.Add( bSizer181, 1, wx.EXPAND, 5 )

        bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText10 = wx.StaticText( self.food_wars_panel, wx.ID_ANY, _(u"Enter Food 5 Here"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText10.Wrap( -1 )

        bSizer191.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.fw_f5_in = wx.TextCtrl( self.food_wars_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer191.Add( self.fw_f5_in, 1, wx.ALL, 5 )


        bSizer121.Add( bSizer191, 1, wx.EXPAND, 5 )

        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( self.food_wars_panel, wx.ID_ANY, _(u"Choose A Nutrition"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer20.Add( self.m_staticText9, 0, wx.ALL, 5 )

        nutin_inputChoices = [ _(u"Caloric Value"), _(u"Fat"), _(u"Saturated Fats"), _(u"Monounsaturated Fats"), _(u"Polyunsaturated Fats"), _(u"Carbohydrates"), _(u"Sugars"), _(u"Protein"), _(u"Dietary Fiber"), _(u"Cholesterol"), _(u"Sodium"), _(u"Water"), _(u"Vitamin A"), _(u"Vitamin B1"), _(u"Vitamin B11"), _(u"Vitamin B12"), _(u"Vitamin B2"), _(u"Vitamin B3"), _(u"Vitamin B5"), _(u"Vitamin B6"), _(u"Vitamin C"), _(u"Vitamin D"), _(u"Vitamin E"), _(u"Vitamin K"), _(u"Calcium"), _(u"Copper"), _(u"Iron"), _(u"Magnesium"), _(u"Manganese"), _(u"Phosphorus"), _(u"Potassium"), _(u"Selenium"), _(u"Zinc"), _(u"Nutrition Density") ]
        self.nutin_input = wx.Choice( self.food_wars_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, nutin_inputChoices, 0 )
        self.nutin_input.SetSelection( 0 )
        bSizer20.Add( self.nutin_input, 1, wx.ALL, 5 )


        bSizer121.Add( bSizer20, 1, wx.EXPAND, 5 )

        bSizer21 = wx.BoxSizer( wx.VERTICAL )

        self.fw_compare_button = wx.Button( self.food_wars_panel, wx.ID_ANY, _(u"Compare"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer21.Add( self.fw_compare_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer121.Add( bSizer21, 1, wx.EXPAND, 5 )


        bSizer11.Add( bSizer121, 1, wx.EXPAND, 5 )


        self.food_wars_panel.SetSizer( bSizer11 )
        self.food_wars_panel.Layout()
        bSizer11.Fit( self.food_wars_panel )
        self.m_notebook1.AddPage( self.food_wars_panel, _(u"Food Wars"), False )

        bSizer9.Add( self.m_notebook1, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.search_button.Bind( wx.EVT_BUTTON, self.search_foods )
        self.search_results_list.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_result_select_cell_click )
        self.search_selection_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_nut_select_cell_click )
        self.breakdown_button.Bind( wx.EVT_BUTTON, self.update_breakdown )
        self.food_wars_button.Bind( wx.EVT_BUTTON, self.fill_food_wars )
        self.remove_button.Bind( wx.EVT_BUTTON, self.remove_selected_food )
        self.fw_compare_button.Bind( wx.EVT_BUTTON, self.onclickcompplot )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def search_foods( self, event ):
        event.Skip()

    def on_result_select_cell_click( self, event ):
        event.Skip()

    def on_nut_select_cell_click( self, event ):
        event.Skip()

    def update_breakdown( self, event ):
        event.Skip()

    def fill_food_wars( self, event ):
        event.Skip()

    def remove_selected_food( self, event ):
        event.Skip()

    def onclickcompplot( self, event ):
        event.Skip()


