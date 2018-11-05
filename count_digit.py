#!/usr/bin/env python3

# Function to count the number of digits in a positive integer

def count_digit(n):
    count = 0
    while n != 0:
        count += 1
        n = n//10
    return count

n = -89

if __name__ == '__main__':
    print(count_digit(n))


