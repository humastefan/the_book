
import turtle

bob = t = turtle.Turtle()
lenght = 58

def square(t, lenght):
    """funtia square va face un patrat cu lungimea - lenght"""
    for i in range(4):
        t.fd(lenght)
        t.lt(90)


square(bob, lenght)
turtle.mainloop()