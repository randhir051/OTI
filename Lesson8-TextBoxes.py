#!/usr/bin/env python
import wx
import shlex
import subprocess
import os
# In this lesson you will learn about the wx.TextCtrl, and simple message boxes.
# You are familiar with both of these widgets, and you will likely find them very useful.

class HelloFrame(wx.Frame):

	def __init__(self, parent):

		wx.Frame.__init__(self, parent, wx.ID_ANY, "Our Tiny IDE")

		self.panel = wx.Panel(self)

		self.response = wx.StaticText(self.panel, pos=(310, 50))
		
		
		# A wx.TextCtrl
		# TextCtrl can also take a size=(width, height) argument.
		self.nameBox = wx.TextCtrl(self.panel, pos=(10, 10), size = (300,800),style = wx.TE_MULTILINE)

		self.btnSubmit = wx.Button(self.panel, label="Compile and Run", pos=(310, 10))
		self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmitSimple)


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
         os.system("gnome-terminal -e './a.out'")

# ----------- Main Program Below -----------------

# Define the app
app = wx.App(False)

# Create a regular old wx.Frame
frame = HelloFrame(None)

# Show the frame
frame.Show()

# Make the app listen for clicks and other events
app.MainLoop()
