import turtle

import turtle

def polygon(t: turtle.Turtle, n: int, length: float):
   angle = 360 / n
   polyline(t, n, length, angle)




def arc(t: turtle.Turtle, radius: float, angle: float):
   arc_length = 2 * math.pi * radius * angle / 360
   n = int(arc_length / 3) + 1
   step_length = arc_length / n
   step_angle = angle / n
   polyline(t, n, step_length, step_angle)

