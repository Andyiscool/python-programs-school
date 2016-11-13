from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="", outline="blue")
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_polygon(300, 20, 360, 40, 270, 100, 170, 230, fill="", outline="white")
