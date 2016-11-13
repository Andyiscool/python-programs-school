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
canvas.create_text(150, 100, text='There once was a man from Toulouse,')
canvas.create_text(130, 120, text='who rode around on a moose.', fill='red')
canvas.create_text(150, 150, text='He said, "It\'s my curse,',
font=('Times', 15))
canvas.create_text(200, 200, text='But it can be worse,',
font=('Helvetica', 20))
canvas.create_text(220, 250, text='My cousin rides around,',
font=('courier', 22))
canvas.create_text(220, 300, text='on a goose"', font=('courier', 30))

from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
canvas.create_polygon(400, 30, 600, 50, 100, 180, 500, 600, fill="", outline="black")
canvas.create_text(140, 120, text='wheres Andy')
canvas.create_text(160, 140, text='is Andy over there?', fill='blue')
canvas.create_text(140, 170, text='hello Andy,',
font=('Times New Roman', 40))
canvas.create_text(120, 200, text='Andy is nice"', font=('Helvetica', 60))
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(300, 10, 340, 10, 340, 50, 300, 50, fill="", outline="blue")


