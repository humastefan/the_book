import turtle
import math
import polygon.py



def circle(t, r):
    """funtia circle va face un cerc cu lungimea - lenght"""
    circumferinta = 2 * math.pi * r
    n = 25
    lenght = circumferinta / n
    poligon(t, n, lenght)


circle(t,654)

turtle.mainloop()