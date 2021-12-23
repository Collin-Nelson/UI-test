import wx

from Serial import SerialComms


class PosesQueuePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, pos=(415, 5), size=(200, 465), style=wx.SUNKEN_BORDER)

        title = wx.StaticText(self, label="Pose Queue", pos=(5, 5), size=(200, 20), style=wx.ALIGN_LEFT)
        self.SetBackgroundColour('white')
        font = title.GetFont()
        font.PointSize = 12
        font = font.Bold()
        title.SetFont(font)

        global tcQueue
        tcQueue = wx.TextCtrl(self, pos=(5, 30), size=(185, 355), style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)

        # Button to run or clear or save or load the pose queue
        runAllBtn = wx.Button(self, label='Run Queue', pos=(5, 430), size=(90, 30))
        clearAllBtn = wx.Button(self, label='Clear Queue', pos=(100, 395), size=(90, 30))
        saveAllBtn = wx.Button(self, label='Save Queue', pos=(5, 395), size=(90, 30))
        loadQueueBtn = wx.Button(self, label='Load Queue', pos=(100, 430), size=(90, 30))

        # Bind buttons to their actions
        runAllBtn.Bind(wx.EVT_BUTTON, self.runAllBtnPress)
        clearAllBtn.Bind(wx.EVT_BUTTON, self.clearAllBtnPress)
        saveAllBtn.Bind(wx.EVT_BUTTON, self.saveAllBtnPress)
        loadQueueBtn.Bind(wx.EVT_BUTTON, self.loadQueueBtnPress)

    # Actions for button
    def runAllBtnPress(self, event):
        num = tcQueue.GetNumberOfLines()
        for i in range(num - 1):
            lineLen = tcQueue.GetLineLength(0)
            # SerialComms.SerialWrite(tcQueue.GetLineText(0))
            print(tcQueue.GetLineText(0))
            tcQueue.Remove(0, lineLen + 2)

    def clearAllBtnPress(self, event):
        while tcQueue.GetNumberOfLines() > 1:
            len = tcQueue.GetLineLength(0)
            tcQueue.Remove(0, len + 2)

    def saveAllBtnPress(self, event):
        dialog = wx.FileDialog(self, 'Choose a file')
        if dialog.ShowModal() == wx.ID_OK:
            self.filename = dialog.GetFilename()
            savefile = open(self.filename, 'w')  # open the file (self.filename) to store our saved data
            savefile.write(
                tcQueue.GetValue())  # get our text from the textctrl, and write it out to the file we just opened.
            savefile.close()  # and then close the file.

    def loadQueueBtnPress(self, event):
        dialog = wx.FileDialog(self, 'Choose a File')
        if dialog.ShowModal() == wx.ID_OK:
            self.filename = dialog.GetFilename()
            loadfile = open(self.filename, 'r')
            lines = loadfile.readlines()
            for line in lines:
                tcQueue.write(line)
            loadfile.close()

    def AddToQueue(string):
        tcQueue.write(string)
