from tkinter import *

def printName():
	print("Milan")

window = Tk()

button = Button(
		window,
		text = "Click",
		command = printName
	)
button.pack()

window.mainloop()