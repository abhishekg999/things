from Tkinter import *
import os

root = Tk()

def tprint():
	os.system("osascript -e 'display dialog (\"YAY\")'")

def rprint(event):
	os.system("osascript -e 'display dialog (\"YAY\")'")

topFrame = Frame(root)
topFrame.pack()

label1 = Label(topFrame, text = "Username")
entry1 = Entry(topFrame)

label2 = Label(topFrame, text = "Password")
entry2 = Entry(topFrame)

c = Checkbutton(topFrame, text="Keep me logged in")

button1 = Button(topFrame, text = "Button 1", command=tprint)
button2 = Button(topFrame, text = "Button 2")
button3 = Button(topFrame, text = "Button 3")
button4 = Button(topFrame, text = "Button 4")

button2.bind("<Button-2>", rprint)




label1.grid(row=0, sticky=E)
entry1.grid(row=0, column=1)
label2.grid(row=1, sticky=E)
entry2.grid(row=1, column=1)
c.grid(row=2, sticky=W)
button1.grid(row=4, column=1, sticky=W)
button2.grid(row=5, column=1, sticky=W)
button3.grid(row=6, column=1, sticky=W)
button4.grid(row=7, column=1, sticky=W)

root.mainloop()

