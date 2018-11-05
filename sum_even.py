#!/usr/bin/env python3

# Function to sum up all even numbers in a list

def sum_even(ls):
    sum = 0
    for i in ls:
        if i%2 == 0:
            sum += i 
    print("The sum of the even numbers in the list is ", sum, ".")


ls = [12, 10, 32, 3, 66, 17, 42, 99, 20]
if __name__ == '__main__':
    sum_even(ls)

