#!/usr/bin/env python3

# Function to sum all the elements in a list up to but not including the first even number

def sum_element(ls):
    sum = 0
    for i in ls:    
        if i%2 != 0:
            sum += i 
        else:
            break

    return sum


ls = [3, 5, 9, 5]
if __name__ == '__main__':
    print(sum_element(ls))
