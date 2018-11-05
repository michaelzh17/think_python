#!/usr/bin/env python3

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

print(is_between(3, 8, 12))
print(is_between(9, 7, 13))
