import wx


class PoseGeneratorPanel(wx.Panel):
    def __init__(self, parent, poses_queue_panel):
        wx.Panel.__init__(self, parent=parent, pos=(620, 5), size=(200, 275), style=wx.SUNKEN_BORDER)

        self.poses_queue_panel = poses_queue_panel

        title = wx.StaticText(self, label="Pose Angle Inputs", size=(200, 18), style=wx.ALIGN_CENTER_HORIZONTAL)
        self.SetBackgroundColour('white')

        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        # Labels for the joint angle text boxes
        lbl1 = wx.StaticText(self, label="J1", pos=(20, 35))
        lbl2 = wx.StaticText(self, label="J2", pos=(20, 65))
        lbl3 = wx.StaticText(self, label="J3", pos=(20, 95))
        lbl4 = wx.StaticText(self, label="J4", pos=(20, 125))
        lbl5 = wx.StaticText(self, label="J5", pos=(20, 155))
        lbl6 = wx.StaticText(self, label="J6", pos=(20, 185))

        # Set the font of the labels on the joint angle display textctrl boxes
        lblfont = lbl1.GetFont()
        lblfont.PointSize = 10
        lblfont = lblfont.Bold()
        lbl1.SetFont(lblfont)
        lbl2.SetFont(lblfont)
        lbl3.SetFont(lblfont)
        lbl4.SetFont(lblfont)
        lbl5.SetFont(lblfont)
        lbl6.SetFont(lblfont)

        # Text input boxes for the angle for each joint
        self.tc1 = wx.TextCtrl(self, pos=(50, 30))
        self.tc2 = wx.TextCtrl(self, pos=(50, 60))
        self.tc3 = wx.TextCtrl(self, pos=(50, 90))
        self.tc4 = wx.TextCtrl(self, pos=(50, 120))
        self.tc5 = wx.TextCtrl(self, pos=(50, 150))
        self.tc6 = wx.TextCtrl(self, pos=(50, 180))

        # Button to to add pose to the queue
        btn1 = wx.Button(self, label='Add to Queue', pos=(15, 210), size=(175, 30))

        # Buttons to add command to open and close gripper to queue
        btn2 = wx.Button(self, label='Open Gripper', pos=(15, 245), size=(85, 30))
        btn3 = wx.Button(self, label='Close Gripper', pos=(105, 245), size=(85, 30))

        # Bind buttons to actions
        btn1.Bind(wx.EVT_BUTTON, self.btn1_press)
        btn2.Bind(wx.EVT_BUTTON, self.btn2_press)
        btn3.Bind(wx.EVT_BUTTON, self.btn3_press)

    # Actions for button
    def btn1_press(self, event):
        print("Add to queue button pressed")
        value1 = self.tc1.GetValue()
        value2 = self.tc2.GetValue()
        value3 = self.tc3.GetValue()
        value4 = self.tc4.GetValue()
        value5 = self.tc5.GetValue()
        value6 = self.tc6.GetValue()

        # set null values to zero
        if value1 == "":
            value1 = "0"
        if value2 == "":
            value2 = "0"
        if value3 == "":
            value3 = "0"
        if value4 == "":
            value4 = "0"
        if value5 == "":
            value5 = "0"
        if value6 == "":
            value6 = "0"

        # Clear the values in the cells
        self.tc1.SetValue("")
        self.tc2.SetValue("")
        self.tc3.SetValue("")
        self.tc4.SetValue("")
        self.tc5.SetValue("")
        self.tc6.SetValue("")

        self.poses_queue_panel.add_to_queue("1:" + value1 + ".2:" + value2 + ".3:" +
                                            value3 + ".4:" + value4 + ".5:" + value5 + ".6:" + value6 + "\n")

    def btn2_press(self, event):
        print("Open gripper button pressed")
        self.poses_queue_panel.add_to_queue("7:180\n")

    def btn3_press(self, event):
        print("Close gripper button pressed")
        self.poses_queue_panel.add_to_queue("7:0\n")
