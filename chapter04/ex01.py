import math
import turtle
bob = turtle.Turtle()
turtle.pendown()

def polyline(t: turtle.Turtle, n: int, length: float, angle: float):
   """Рисует n отрезков с заданной длиной length и углами angle
   (в градусах) между ними черепашкой t.
   """
   for i in range(n):
       t.forward(length)
       t.left(angle)

def circle(t: turtle.Turtle, radius: float):
    arc(t, radius, 360)

def arc(t: turtle.Turtle, radius: float, angle: float):
   arc_length = 2 * math.pi * radius * abs(angle) / 360
   n = int(arc_length / 4) + 3
   step_length = arc_length / n
   step_angle = angle / n
   t.left(step_angle / 2)
   polyline(t, n, step_length, step_angle)
   t.right(step_angle / 2)

#polygon(bob, n=7, length=70)
circle(bob, 100)
turtle.mainloop()
