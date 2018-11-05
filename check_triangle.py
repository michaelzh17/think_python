#!/usr/bin/env python3

def is_triangle(a, b, c):
    if a > b+c or b > a+c or c > a+b:
        return "No"
    else:
        return "Yes"

def check_triangle():
    a = int(input("give me an integer: "))
    b = int(input("give me a second integer: "))
    c = int(input("give me a third integer: "))
    return is_triangle(a, b, c)

print(check_triangle())

