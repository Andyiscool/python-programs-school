from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 60, 60, 60, 10)
def movesquare(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(1, -5, 0)
    else:
        canvas.move(1, 5, 0)
canvas.bind_all('<KeyPress-Up>', movesquare)
canvas.bind_all('<KeyPress-Down>', movesquare)
canvas.bind_all('<KeyPress-Left>', movesquare)
canvas.bind_all('<KeyPress-Right>', movesquare)
