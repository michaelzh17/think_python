#!/usr/bin/env python3

# Print True if all the numbers in the list are odd

def true_odd(ls):
    count = 0
    for number in ls:
        count += number % 2 == 0
    print(count == 0)
  


ls = [3, 5, 17, 23, 57, 68]

if __name__ == '__main__':
    true_odd(ls)


