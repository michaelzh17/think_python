#!/usr/bin/env python3

# test if in a condition the function goes to end without a return statement

def test(x):
    if x > 0:
        return x
    if x < 0:
        return -x 

print(test(9))
print(test(-6))
print(test(0)) 
