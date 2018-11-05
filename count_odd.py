#!/usr/bin/env python3

# A function to count the odd numbers in a list


def count_odd(ls):
    count = 0
    for i in ls:
        if i%2 != 0:
            count += 1
    print("There are ", count, " odd numbers in the list.")


ls = [12, 10, 32, 3, 66, 17, 42, 99, 20]
if __name__ == '__main__':
    count_odd(ls)
