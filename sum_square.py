#!/usr/bin/env python3


# Function to sum the squares of numbers in a list

def sum_square(ls):
    sum = 0
    for i in ls:
        sum += i*i 
    return sum

ls = [3, 5, 9]

if __name__ == '__main__':
    print(sum_square(ls))


        
