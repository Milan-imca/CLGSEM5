from tkinter import *

window = Tk()
# window.geometry("500x500")

canvas = Canvas(window,bg="white",height=500,width=500)
canvas.pack()

canvas.create_rectangle((10,10,250,250),fill="blue")
# canvas.create_rectangle((249,10,499,250),fill="blue")
canvas.create_arc(10,251,251,200)
window.mainloop()

