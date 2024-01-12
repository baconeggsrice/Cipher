import wx

class guiFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Cipher')
        self.show()

if __name__ == '__main__':
    app = wx.App()
    frame = guiFrame()
    app.MainLoop()