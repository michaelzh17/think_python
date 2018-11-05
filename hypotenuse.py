#!/usr/bin/env python3

import math

def hypotenuse(x, y):
    h_square = x**2 + y**2
    print("the square of the hypotenuse is: ", h_square)
    h = math.sqt(h_square)
    return h

print(hypotenuse(3, 4))

