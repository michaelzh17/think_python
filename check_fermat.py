#!usr/bin/env python3

def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        return "Holy smokes, Fermat was wrong!"
    else:
        return "No, that doesn't work."

def prompt_check():
    a = int(input("give me an integer: "))
    b = int(input("give me a second integer: "))
    c = int(input("give me a third integer: "))
    n = int(input("give me the fourth integer: "))
    
    return check_fermat(a, b, c, n)

print(prompt_check())

