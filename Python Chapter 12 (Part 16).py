from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
mysquare = canvas.create_polygon(10, 10, 10, 60, 60, 60, 60, 10,
fill='yellow')
canvas.itemconfig(mysquare, fill='blue')
canvas.itemconfig(mysquare, outline='yellow')
