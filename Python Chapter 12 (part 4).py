from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=700, height=700)
canvas.pack()
canvas.create_arc(30, 30, 800, 700, extent=180, style=ARC)
