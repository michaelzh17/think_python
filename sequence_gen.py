#!/usr/bin/env python3

# Function to generate sequence: starting with n, then following with halving n, if n is even 
# or n multiply by 3 and add 1, the sequence ends when n is 1

def sequence_gen(n):
    while n != 1:
        print(n,end = ",  ")

        if n%2 == 0:
            n = n//2
        else:
            n = n * 3 + 1
    print(n,end = ".\n")

n = 3

if __name__ == '__main__':
    sequence_gen(n)

