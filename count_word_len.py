#!/usr/bin/env python3

# Function to count the number of words with length as 5 in the list

def count_words(words):
    count = 0
    for word in words:
        if len(word) == 5:
            count += 1
    print("There are ", count, "words in the list having length as 5")


if __name__ == '__main__':
    count_words(words)


