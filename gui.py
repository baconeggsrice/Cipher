import wx

class guiFrame(wx.Frame):
    def __init__(self,*args, **kwargs):
        super(guiFrame, self).__init__(*args, **kwargs)
        panel = wx.Panel(self)
        self.InitUI(panel)
        self.msgToEncode(panel)
        self.letters = {1:'', 2:''}

    def InitUI(self,panel):

        #wx.CallLater(3000, self.ShowMessage)
        self.comboBox(panel)
        self.SetSize((300, 200))
        self.SetTitle('Message box')
        self.Centre()

    def msgToEncode(self, panel): #Temp for message submission
        self.text_ctrl = wx.TextCtrl(panel, pos = (5,35))
        self.button = wx.Button(panel, label = "Generate", pos = (5,60))
        self.msgSt = wx.StaticText(panel, label = 'test', pos=(5,85))

    def ShowMessage(self):
        wx.MessageBox('msg', 'Encoded Message', wx.OK | wx.ICON_INFORMATION)

    def comboBox(self, panel):
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        box1 = wx.ComboBox(panel, pos=(5,5), choices = alphabet, style=wx.CB_READONLY)
        box2 = wx.ComboBox(panel, pos=(55,5), choices = alphabet, style=wx.CB_READONLY)
        self.st1 = wx.StaticText(panel, label='', pos=(5,125))
        self.st2 = wx.StaticText(panel, label='', pos=(35,125))
        box1.Bind(wx.EVT_COMBOBOX, self.box1Triggered)
        box2.Bind(wx.EVT_COMBOBOX, self.box2Triggered)

    def box1Triggered(self, guiFrame):
        letter1 = guiFrame.GetString()
        print(letter1)
        self.st1.SetLabel(letter1)
        self.letters[1] = letter1
        #print(self.letters)

    def box2Triggered(self, guiFrame):
        letter2 = guiFrame.GetString()
        print(letter2)
        self.st2.SetLabel(letter2)
        self.letters[2] = letter2
        #print(self.letters)

    def ctrlBoxTriggered(self, guiFrame):
        msg = guiFrame.GetString()
        print(msg)
        self.msgSt.SetLabel(msg)

def main():
    app = wx.App()
    frame = guiFrame(None)
    frame.Show()
    print(frame.letters)
    app.MainLoop()

if __name__ == '__main__':
    main()