#!/usr/bin/env python
import wx
import shlex
import subprocess
import os
# In this lesson you will learn about the wx.TextCtrl, and simple message boxes.
# You are familiar with both of these widgets, and you will likely find them very useful.

class HelloFrame(wx.Frame):

    terminal = ""
    def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Our Tiny IDE")
		self.panel = wx.Panel(self)
		self.response = wx.StaticText(self.panel, pos=(310, 50))
		
		# A wx.TextCtrl
		# TextCtrl can also take a size=(width, height) argument.
		self.nameBox = wx.TextCtrl(self.panel, pos=(10, 10), size = (300,800),style = wx.TE_MULTILINE)

		self.btnSubmit = wx.Button(self.panel, label="Compile and Run", pos=(310, 10))
		self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmitSimple)
                self.cbShowTitle = wx.CheckBox(self.panel, label='Sticky Terminal', pos=(310, 80))
		self.cbShowTitle.SetValue(True)
		self.cbShowTitle.Bind(wx.EVT_CHECKBOX, self.OnToggleShowTitle)
                global terminal
                terminal = "gnome-terminal -e 'bash -c \"./a.out; exec bash\"'"

    def OnToggleShowTitle(self, e):
        global terminal
        isChecked = self.cbShowTitle.GetValue()
        if isChecked:
			terminal = "gnome-terminal -e 'bash -c \"./a.out; exec bash\"'"
        else:
			terminal = "gnome-terminal -e './a.out'"
    def OnSubmitSimple(self, e):
         nameString = self.nameBox.GetValue()
         Write(nameString)

def Write(codeString):
         outfile = open("hello.c",'w')
         outfile.write(codeString)
         outfile.close()
         # cmd = ["gcc", "-O2", "hello.c", "-o", "hello"]
         # args = shlex.split(cmd)
         # proc = Popen(args, stdout=PIPE, stderr=PIPE)
         # out, err = proc.communicate()
         # exitcode = proc.returncode
         subprocess.check_output(["gcc","hello.c"])
         global terminal
         os.system(terminal)


# Define the app
app = wx.App(False)

# Create a regular old wx.Frame
frame = HelloFrame(None)

# Show the frame
frame.Show()

# Make the app listen for clicks and other events
app.MainLoop()
