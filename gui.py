import wx
import ceasarCipher

class guiFrame(wx.Frame):
    def __init__(self,*args, **kwargs):
        super(guiFrame, self).__init__(*args, **kwargs)
        panel = wx.Panel(self)
        self.InitUI(panel)
        self.msgToEncode(panel)
        self.msgToDecode(panel)
        self.info = {1:'', 2:'', 3:''}
        self.decodeInfo = {1:'', 2:'', 3:''}
        self.clicked = False
        self.message = ''

    def InitUI(self,panel):
        self.comboBox(panel)
        self.decodeComboBox(panel)
        self.SetSize((300, 250))
        self.SetTitle('Message box')
        self.Centre()

    def msgToEncode(self, panel): #Temp for message submission
        self.text_ctrl = wx.TextCtrl(panel, pos = (5,35))
        self.button = wx.Button(panel, label = "Generate", pos = (5,60))
        self.button.Bind(wx.EVT_BUTTON, self.ctrlBoxTriggered)

    def ShowMessage(self):
        wx.MessageBox(self.message, 'Encoded Message', wx.OK | wx.ICON_INFORMATION)

    def comboBox(self, panel):
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        box1 = wx.ComboBox(panel, pos=(5,5), choices = alphabet, style=wx.CB_READONLY)
        box2 = wx.ComboBox(panel, pos=(55,5), choices = alphabet, style=wx.CB_READONLY)
        box1.Bind(wx.EVT_COMBOBOX, self.box1Triggered)
        box2.Bind(wx.EVT_COMBOBOX, self.box2Triggered)

    def box1Triggered(self, guiFrame):
        letter1 = guiFrame.GetString()
        self.info[1] = letter1
        print(self.clicked)
        print(self.info)

    def box2Triggered(self, guiFrame):
        letter2 = guiFrame.GetString()
        self.info[2] = letter2
        print(self.clicked)
        print(self.info)

    def ctrlBoxTriggered(self, event):
        msg = self.text_ctrl.GetValue()
        self.clicked = True
        self.info[3] = msg
        print(self.clicked)
        print(self.info)
        if self.info[3] == "Guess What": #Easter Egg Fun
            self.message = "Chicken Butt"
        else:
            self.message = ceasarCipher.cipherMain(self.info)
        print(self.message, msg)
        wx.CallLater(1000, self.ShowMessage)


     ###### DECODING ########
    def msgToDecode(self, panel): #Temp for message submission
        self.text_ctrl = wx.TextCtrl(panel, pos = (5,140))
        self.button = wx.Button(panel, label = "Decode", pos = (5,165))
        self.button.Bind(wx.EVT_BUTTON, self.decodeBoxTriggered)   

    def decodeComboBox(self, panel):
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        box3 = wx.ComboBox(panel, pos=(5,105), choices = alphabet, style=wx.CB_READONLY)
        box4 = wx.ComboBox(panel, pos=(55,105), choices = alphabet, style=wx.CB_READONLY)
        box3.Bind(wx.EVT_COMBOBOX, self.box3Triggered)
        box4.Bind(wx.EVT_COMBOBOX, self.box4Triggered)

    def box3Triggered(self, guiFrame):
        letter3 = guiFrame.GetString()
        self.decodeInfo[1] = letter3
        print(self.clicked)
        print(self.decodeInfo)

    def box4Triggered(self, guiFrame):
        letter4 = guiFrame.GetString()
        self.decodeInfo[2] = letter4
        print(self.clicked)
        print(self.decodeInfo)

    def decodeBoxTriggered(self, event):
        dmsg = self.text_ctrl.GetValue()
        self.clicked = True
        self.decodeInfo[3] = dmsg
        print(self.clicked)
        print(self.decodeInfo)
        self.message = ceasarCipher.decoding(self.decodeInfo)
        print(self.message, dmsg)
        wx.CallLater(1000, self.ShowDecoded)

    def ShowDecoded(self):
        wx.MessageBox(self.message, 'Decoded Message', wx.OK | wx.ICON_INFORMATION)

def main():
    app = wx.App()
    frame = guiFrame(None)
    frame.Show()
    print(frame.info)
    app.MainLoop()

if __name__ == '__main__':
    main()