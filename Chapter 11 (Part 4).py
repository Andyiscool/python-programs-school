import turtle
t =turtle.Pen()
def mysquare(size):
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
mysquare(50)
t.reset()
mysquare(25)
mysquare(50)
mysquare(75)
mysquare(100)
mysquare(125)
t.reset()
t.begin_fill()
mysquare(50)
t.end_fill()
def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
mysquare(50, True)
mysquare(150, False)
t.reset()
for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
t.reset()
def mystar(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()
t.color(0.9, 0.75, 0)
mystar(120, True)
t.color(0,0,0)
mystar(120, False)
t.reset()
for x in range(1, 9):
    t.forward(100)
    t.left(45)
t.reset()
def myoctagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()
t.color(0.9, 0.75, 0)
myoctagon(100, True)
t.color(0,0,0)
myoctagon(100, False)
t.reset()
def draw_star(size, points):
    for x in range(80, 70):
        t.forward(100)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)

