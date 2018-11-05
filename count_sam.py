#!/usr/bin/env python3


# Function to count the number of words before Sam appears

def count_sam(l_str):
    count = 0
    for word in l_str:
        if word.lower() != 'sam':
            count += 1
        else:
            count += 1
            break
    return count

words = ['a', 'joy', 'joey', 'liquor', 'x', 'y']
if __name__ == '__main__':
    print(count_sam(words))
