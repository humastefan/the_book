import turtle
import math
t = turtle.Turtle()


def arc(t, r, angle):
    arc_lenght = 2 * math.pi *r * angle / 360
    n = int(arc_lenght/3) + 1
    step_lenght = arc_lenght/n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_lenght)
        t.lt(step_angle)

#arc(t,90,270)

def polyline(t, n, lenght, angle):
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)

#polyline(t, 7, 90, 30)

def polygon(t, n, lenght):
    angle = 360.0 / n
    polyline(t, n, lenght, angle)

#polygon(t, 7, 130)

def arcul(t, r, angle):
    arc_lenght = 2 * math.pi *r * angle / 360
    n = int(arc_lenght/3) + 1
    step_lenght = arc_lenght/n
    step_angle = angle / n
    polyline(t, n, step_lenght, step_angle)

#arcul(t, 130, 180)

def circle(t, r):
    arcul(t, r, 360)

#circle(t, 90)

for i in range(50, 150, 20):
    circle(t, i)
    arcul(t, i, 78)

turtle.mainloop()