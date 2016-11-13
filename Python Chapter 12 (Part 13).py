
Python 3.4.3 (default, Sep 14 2016, 12:36:27) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/andyxiao/Python Programs/Python Chapter 12(Part 12).py", line 15, in <module>
    canvas.bind_all('<KeyPress-Up>', movetriangle)
NameError: name 'movetriangle' is not defined
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_polygon(10, 10, 10, 60, 50, 35)
1
>>> canvas.move(1, 5, 0)
