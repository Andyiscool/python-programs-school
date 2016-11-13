Python 3.4.3 (default, Sep 14 2016, 12:36:27) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_polygon(10, 10, 10, 60, 60, 60, 60, 10)
1
>>> canvas.move(1, 10, 100)
>>> canvas.move(1, 100, 100)
>>> canvas.move(1, 100, 100)
>>> 
