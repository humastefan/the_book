import turtle
#import mypolygon.py
t=turtle.Turtle()
lenght = 324
import patrat.py

n=14
def polygon(t, lenght,n):
   for i in range(n):
      t.fd(lenght)
      t.lt(360/n)

#polygon(t,lenght,n)

r=21
def circle(t, r):
   polygon(t,40,r)

#circle(t, r)

def arc(t, r, angle):
   polygon(t,360/angle,r)

#arc(t, r, 15)

turtle.mainloop()
