import turtle
import random

pen = turtle.Turtle()
pen.speed(0)

def screensaver(n,length):
    for i in range(length, 0, -10):
        pen.fd(i)
        pen.left(360 / n)

screensaver(5,200)
turtle.mainloop()