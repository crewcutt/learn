import math
import turtle
from cmath import sqrt

bob = turtle.Turtle()
bob.pendown()
bob.speed(0)
size = 30
diagonal = size * math.sqrt(2)

"""функции движени я по 8 географическим направлениями 
    n - ↑ North  
    w - ← West 
    nw - ↖ North West
    s -
    e - ...
"""

def w(t: turtle.Turtle, step: int):
    t.left(180)
    t.forward(size*step)
    t.right(180)

def e(t: turtle.Turtle, step: int):
    t.forward(size*step)

def n(t: turtle.Turtle, step: int):
    t.left(90)
    t.forward(size*step)
    t.right(90)

def ne(t: turtle.Turtle, step: int):
    t.left(45)
    t.forward(diagonal*step)
    t.right(45)

def nw(t: turtle.Turtle, step: int):
    t.left(135)
    t.forward(diagonal*step)
    t.right(135)

def s(t: turtle.Turtle, step: int):
    t.left(270)
    t.forward(size*step)
    t.right(270)

def se(t: turtle.Turtle, step: int):
    t.left(315)
    t.forward(diagonal*step)
    t.right(315)

def sw(t: turtle.Turtle, step: int):
    t.left(225)
    t.forward(diagonal*step)
    t.right(225)

def pen(t, tail: int): # подъем пера по "0"
    if tail == 0:
        t.penup()
    else:
        t.pendown()

def space(t):
        t.penup()
        t.forward(size)
        t.pendown()


def print_a(t: turtle.Turtle):
    n(t,1)
    ne(t,1)
    s(t,1)
    w(t,1)
    e(t,1)
    s(t,1)
    space(t)

def print_b(t: turtle.Turtle):
    e(t, 1)
    n(t,1)
    w(t,1)
    s(t,1)
    n(t,2)
    e(t, 1)
    pen(t, 0)
    s(t, 2)
    pen(t, 1)
    space(t)

def print_B(t: turtle.Turtle):
    n(t, 2)
    se(t,1)
    w(t,1)
    se(t, 1)
    w(t,1)
    e(t, 1)
    pen(t, 0)
    space(t)

print_a(bob)
print_a(bob)
print_b(bob)
print_B(bob)

turtle.mainloop()
