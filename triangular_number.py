#!/usr/bin/env python3

# Function to print out number and its triangular

def triangular(n):
    tri_num = 0
    for i in range(n):
        tri_num += i+1
        print(i+1, tri_num)


if __name__ == '__main__':
    triangular(6)


