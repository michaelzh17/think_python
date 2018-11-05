#!/usr/bin/env python3

# Demo of use of break

# Does the list have any odd numbers?

numbers = [6, 8, 34,7, 18]

for number in numbers:
    if number%2 == 1:
        print(True)
        break
else:
    print(False)


count = 0 

for number in numbers:
    if number%2 == 1:
        count += 1
print(count > 0)


counter = 0

for number in numbers:
    counter += number%2 == 1
print(count > 0)


