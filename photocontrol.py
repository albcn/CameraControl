#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun Nov  6 17:05:21 2011

import wx

import photocontrolnx

# begin wxGlade: extracode
# end wxGlade



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.GuiController_statusbar = self.CreateStatusBar(4, 0)
        self.bt_initCam = wx.Button(self, -1, "Initialize Camera")
        self.labelNull = wx.StaticText(self, -1, "")
        self.lab_shots = wx.StaticText(self, -1, "Num. Shots", style=wx.ALIGN_RIGHT)
        self.sc_setShots = wx.SpinCtrl(self, -1, "", min=0, max=100)
        self.lab_interval = wx.StaticText(self, -1, "Interval (s)", style=wx.ALIGN_RIGHT)
        self.sc_setInterval = wx.SpinCtrl(self, -1, "", min=0, max=100)
        self.lab_filenamebase = wx.StaticText(self, -1, "File Name Base")
        self.inp_filebasename = wx.TextCtrl(self, -1, "capture")
        self.lab_figurestyle = wx.StaticText(self, -1, "Current Picture Style")
        self.combo_pictureStyle = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.static_line_3 = wx.StaticLine(self, -1)
        self.static_line_4 = wx.StaticLine(self, -1)
        self.lab_over = wx.StaticText(self, -1, "Overexposition \ncomp  (for HDR-TL)")
        self.combo_hdr = wx.ComboBox(self, -1, choices=[], style=wx.CB_DROPDOWN)
        self.tog_previewCaps = wx.ToggleButton(self, -1, "Preview Captures")
        self.lab_preview = wx.StaticText(self, -1, "")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.static_line_2 = wx.StaticLine(self, -1)
        self.but_startCapture = wx.Button(self, -1, "Start Capture")
        self.bitmap_2 = wx.StaticBitmap(self, -1, wx.Bitmap("/home/alex/src/CameraControl/back.jpg", wx.BITMAP_TYPE_ANY))
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.guiIniCam, self.bt_initCam)
        self.Bind(wx.EVT_SPINCTRL, self.guiSetShots, self.sc_setShots)
        self.Bind(wx.EVT_SPINCTRL, self.guiSetInterval, self.sc_setInterval)
        self.Bind(wx.EVT_TEXT, self.guiGetFileNameBase, self.inp_filebasename)
        self.Bind(wx.EVT_TEXT_ENTER, self.guiPictureStyle, self.combo_pictureStyle)
        self.Bind(wx.EVT_COMBOBOX, self.guiPictureStyle, self.combo_pictureStyle)
        self.Bind(wx.EVT_TEXT_ENTER, self.guiHDR, self.combo_hdr)
        self.Bind(wx.EVT_COMBOBOX, self.guiHDR, self.combo_hdr)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.guiTogglePreviewCaptures, self.tog_previewCaps)
        self.Bind(wx.EVT_BUTTON, self.guiStartCapture, self.but_startCapture)
        # end wxGlade
        self.camera = None
        self.capture = None

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("GuiController")
        self.GuiController_statusbar.SetStatusWidths([-1, 100, 50, 50])
        # statusbar fields
        GuiController_statusbar_fields = ["Camera", "Status", "Series", "Current"]
        for i in range(len(GuiController_statusbar_fields)):
            self.GuiController_statusbar.SetStatusText(GuiController_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.FlexGridSizer(11, 2, 1, 1)
        grid_sizer_1.Add(self.bt_initCam, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.labelNull, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.lab_shots, 0, 0, 0)
        grid_sizer_1.Add(self.sc_setShots, 0, 0, 0)
        grid_sizer_1.Add(self.lab_interval, 0, 0, 0)
        grid_sizer_1.Add(self.sc_setInterval, 0, 0, 0)
        grid_sizer_1.Add(self.lab_filenamebase, 0, 0, 0)
        grid_sizer_1.Add(self.inp_filebasename, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.lab_figurestyle, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.combo_pictureStyle, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.static_line_3, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.static_line_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.lab_over, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.combo_hdr, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.tog_previewCaps, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.lab_preview, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.static_line_2, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.but_startCapture, 0, wx.EXPAND, 0)
        sizer_3.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_3.Add(self.bitmap_2, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_2.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

    def guiIniCam(self, event): # wxGlade: MyFrame.<event_handler>
        print "guiIniCam"
        #Iniciatlitzem les clases de control de la camara
        self.camera = photocontrolnx.Camera()
        self.capture = photocontrolnx.Capture(self.camera)
        #Busquem les compensacions d'exposicio disponibles a la camara
        def f(x): 
            return not('-' in x)
        comps = filter(f,  self.camera.compensations)
        comps.sort()
        # Les injectem al widget
        self.combo_hdr.Clear()
        [self.combo_hdr.Append(x) for x in comps]
        # Seleccionem el que es actual
        if self.capture.getHDR() == None:
            self.combo_hdr.SetValue(u"0")
        else:
            self.combo_hdr.SetValue(self.capture.getHDR())
            
        # Un procediment similar pel picturesytle
        self.combo_pictureStyle.Clear()
        [self.combo_pictureStyle.Append(x) 
            for x in self.capture.getPictureStyles()]
        self.combo_pictureStyle.SetValue(self.capture.getPictureStyle())
        (self.capture.getPictureStyle)
        
        # Fitxem shots i interval inicials
        self.sc_setShots.SetValue(self.capture.getShots())
        self.sc_setInterval.SetValue(self.capture.getInterval())

        event.Skip()

    def guiSetShots(self, event): # wxGlade: MyFrame.<event_handler>
        self.capture.setShots(self.sc_setShots.GetValue())
        self.sc_setShots.SetValue(self.capture.getShots())
        event.Skip()

    def guiSetInterval(self, event): # wxGlade: MyFrame.<event_handler>
        self.capture.setInterval(self.sc_setInterval.GetValue())
        self.sc_setInterval.SetValue(self.capture.getInterval())
        event.Skip()

    def guiGetFileNameBase(self, event): # wxGlade: MyFrame.<event_handler>
        self.capture.setFile(self.inp_filebasename.GetValue())
        print self.capture.getFile()
        event.Skip()


    def guiTogglePreviewCaptures(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `guiTogglePreviewCaptures' not implemented!"
        event.Skip()

    def guiStartCapture(self, event): # wxGlade: MyFrame.<event_handler>
        print "Starting Capture"
        self.capture.exeCapture()
        event.Skip()

    def guiPictureStyle(self, event): # wxGlade: MyFrame.<event_handler>
        self.capture.setPictureStyle(self.combo_pictureStyle.GetValue())
        #print self.capture.getPictureStyle()
        event.Skip()

    def guiHDR(self, event): # wxGlade: MyFrame.<event_handler>
        self.capture.setHDR(self.combo_hdr.GetValue())
        print self.capture.getHDR()
        event.Skip()  
# end of class MyFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    GuiController = MyFrame(None, -1, "")
    app.SetTopWindow(GuiController)
    GuiController.Show()
    app.MainLoop()
