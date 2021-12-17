import turtle
import math
t = turtle.Turtle()


def poligon(t, ast, lenght):
    """funtia polygon va face un poligon cu n laturi de lungime lenght"""
    for i in range(ast):
        t.fd(lenght)
        t.lt(360/ast)

poligon(t,7,157)

turtle.mainloop()

def circle(t, r):
    """funtia circle va face un cerc cu lungimea - lenght"""
    circumferinta = 2 * math.pi * r
    n = 25
    lenght = circumferinta / n
    poligon(t, n, lenght)


#circle(t,25)

#turtle.mainloop()