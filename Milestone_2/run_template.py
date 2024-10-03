#This is where the program will run from.

import wx
import template_frame


class MyApp(wx.App):
    def OnInit(self):
        # Create an instance of the frame (your main window)
        frame = template_frame.MyFrame1(None)

        # Show the frame
        frame.Show(True)

        return True


if __name__ == "__main__":
    # Create a wx App instance
    app = MyApp(False)

    # Start the wx event loop
    app.MainLoop()
