import turtle
import math

t = turtle.Turtle()


def square(t, lenght):
    """funtia square va face un patrat cu lungimea - lenght"""
    for i in range(4):
        t.fd(lenght)
        t.lt(90)


def polygon(t, n, lenght):
    angle = 360 / n
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)


def circle(t, r):
    """funtia circle va face un cerc cu lungimea - lenght"""
    circumferinta = 2 * math.pi * r
    n = 50
    lenght = circumferinta / n
    polygon(t, n, lenght)


circle(t, 50)

turtle.mainloop()
