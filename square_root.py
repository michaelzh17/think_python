#!/usr/bin/env python3

# Function to calculate square root of a number

def square_root(n):
    
    approximation = n/2
    threshold = 0.0001
    while True:
        
        better =(approximation + n/approximation)/2
        if abs(approximation - better) < threshold:
            print(str(better) + ' is the square root')
            break
        print(better)
        approximation = better

n = 123

if __name__ == '__main__':
    square_root(n)


     
