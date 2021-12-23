import wx

from Serial import SerialComms


class AngleInputPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, pos=(210, 5), size=(200, 230), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Joint Angle Inputs", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Text input boxes for the angle for each joint
        self.tc1 = wx.TextCtrl(self, pos=(90, 20))
        self.tc2 = wx.TextCtrl(self, pos=(90, 50))
        self.tc3 = wx.TextCtrl(self, pos=(90, 80))
        self.tc4 = wx.TextCtrl(self, pos=(90, 110))
        self.tc5 = wx.TextCtrl(self, pos=(90, 140))
        self.tc6 = wx.TextCtrl(self, pos=(90, 170))

        # Buttons to trigger moving to the specified number of degrees
        btn7 = wx.Button(self, label='Move All', pos=(5, 200), size=(175, 30))
        btn1 = wx.Button(self, label='Move J1', pos=(5, 20))
        btn2 = wx.Button(self, label='Move J2', pos=(5, 50))
        btn3 = wx.Button(self, label='Move J3', pos=(5, 80))
        btn4 = wx.Button(self, label='Move J4', pos=(5, 110))
        btn5 = wx.Button(self, label='Move J5', pos=(5, 140))
        btn6 = wx.Button(self, label='Move J6', pos=(5, 170))


        # Bind each button to its action
        btn1.Bind(wx.EVT_BUTTON, self.btn1Press)
        btn2.Bind(wx.EVT_BUTTON, self.btn2Press)
        btn3.Bind(wx.EVT_BUTTON, self.btn3Press)
        btn4.Bind(wx.EVT_BUTTON, self.btn4Press)
        btn5.Bind(wx.EVT_BUTTON, self.btn5Press)
        btn6.Bind(wx.EVT_BUTTON, self.btn6Press)
        btn7.Bind(wx.EVT_BUTTON, self.btn7Press)

    # Actions for each button
    def btn1Press(self, event):
        value = self.tc1.GetValue()
        if not value:
            print("You didn't enter anything!")

        else:
            print(f'You typed: "{value}"')
            SerialComms.SerialWrite("1:" + value)

    def btn2Press(self, event):
        value = self.tc2.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            SerialComms.SerialWrite("2:" + value)

    def btn3Press(self, event):
        value = self.tc3.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            SerialComms.SerialWrite("3:" + value)

    def btn4Press(self, event):
        value = self.tc4.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            SerialComms.SerialWrite("4:" + value)

    def btn5Press(self, event):
        value = self.tc5.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            SerialComms.SerialWrite("5:" + value)

    def btn6Press(self, event):
        value = self.tc6.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')
            SerialComms.SerialWrite("6:" + value)

    def btn7Press(self, event):
        value1 = self.tc1.GetValue()
        value2 = self.tc2.GetValue()
        value3 = self.tc3.GetValue()
        value4 = self.tc4.GetValue()
        value5 = self.tc5.GetValue()
        value6 = self.tc6.GetValue()

        SerialComms.SerialWrite(
            "1:" + value1 + ".2:" + value2 + ".3:" + value3 + ".4:" + value4 + ".5:" + value5 + ".6:" + value6)
