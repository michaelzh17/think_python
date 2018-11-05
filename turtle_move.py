#!/usr/bin/env python3

import math
import turtle
arrow = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    t.mainloop()

#square(arrow, 80)
    
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    t.mainloop()


#length = 120
#n = 8
#polygon(arrow, length, n) 


def circle(t, r):
    circumference = math.pi*(r**2)
    n = 100
    length = circumference/500
    
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    t.mainloop()

circle(arrow, 20)


