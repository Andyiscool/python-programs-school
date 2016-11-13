from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
myimage = PhotoImage(file='/home/andyxiao/images.png')
canvas.create_image(5, 5, anchor=NW, image=myimage)

