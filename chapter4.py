#!/usr/bin/env python3

# Exercise for Chapter 4

# 1.
print('\nQ1')

def turn_clockwise(direction):
    if direction.upper() == 'N':
        return 'E'
    elif direction.upper() == 'E':
        return 'S'
    elif direction.upper() == 'S':
        return 'W'
    elif direction.upper() == 'W':
        return 'N'
    


print(turn_clockwise('N') == 'E')
print(turn_clockwise('W') == 'N')
print(turn_clockwise('A'))

# 2.
print('\nQ2')

def day_name(i):
    if i == 0:
        return 'Sunday'
    elif i == 1:
        return 'Monday'
    elif i == 2:
        return 'Tuesday'
    elif i == 3:
        return 'Wednesday'
    elif i == 4:
        return 'Thursday'
    elif i == 5:
        return 'Friday'
    elif i == 6:
        return 'Saturday'

print(day_name(1))
print(day_name(9))
print(day_name('a'))


# 3.
print('\nQ3')

def day_num(weekday):
    if weekday.lower() == 'sunday':
        return 0
    elif weekday.lower() == 'monday':
        return 1
    elif weekday.lower() == 'tuesday':
        return 2
    elif weekday.lower() == 'wednesday':
        return 3
    elif weekday.lower() == 'thursday':
        return 4
    elif weekday.lower() == 'friday':
        return 5
    elif weekday.lower() == 'saturday':
        return 6

print(day_num('Tuesday') == 2)
print(day_num('Friday') == 5)
print(day_num('abc') == None)



# 4.
print('\nQ4')

def day_add(day, i):
    return day_name((day_num(day)+i)%7)

print(day_add('Monday', 4) == 'Friday')
print(day_add('Tuesday', 0) == 'Tuesday')
print(day_add('Tuesday', 14) == 'Tuesday')
print(day_add('Sunday', 100) == 'Tuesday')


# 5.
print('\nQ5')

print(day_add('Sunday', -1) == 'Saturday')
print(day_add('Sunday', -7) == 'Sunday')
print(day_add('Tuesday', -100) == 'Sunday')

# 6.
print('\nQ6')
# Return number of days in a month with given month

def days_in_month(month):
    if month.lower() in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
        return 31
    elif month.lower() == 'february':
        return 28
    elif month.lower() in ['april', 'june', 'september', 'november']:
        return 30

print(days_in_month('February') == 28)
print(days_in_month('December') == 31)

# 7.
print('\nQ7')
# Function to convert hours, minutes, seconds to a total number of seconds

def to_secs(hr, min, sec):
    return int(sec + 60*min + 3600*hr)

print(to_secs(2, 30, 10) == 9010)
print(to_secs(2, 0, 0) == 7200)
print(to_secs(0, 2, 0) == 120)
print(to_secs(0, 0, 42) == 42)
print(to_secs(0, -10, 10) == -590)

# 8.
print('\nQ8')

print(to_secs(2.5, 0, 10.71) == 9010)
print(to_secs(2.433, 0, 0) == 8758)

# 9.
print('\nQ9')

def hours_in(secs):
    return int(secs//3600)

def minutes_in(secs):
    return int((secs%3600)//60)

def seconds_in(secs):
    return int(secs%3600%60)

print(hours_in(9010) == 2)
print(minutes_in(9010) == 30)
print(seconds_in(9010) == 10)


# 10.
print('\nQ10')

# Function to compare two integer

def compare(a, b):
    if a > b: 
        return 1
    elif a == b:
        return 0
    else:
        return -1

print(compare(5, 4) == 1)
print(compare(7, 7) == 0)
print(compare(2, 3) == -1)
print(compare(42, 1) == 1)

# 11.
print('\nQ11')

def hypotenuse(a, b):
    return (a**2 + b**2)**0.5

print(hypotenuse(3, 4) == 5.0)
print(hypotenuse(12, 5) == 13)
print(hypotenuse(24, 7) == 25.0)
print(hypotenuse(9, 12)) 

# 12.
print('\nQ12')

def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

print(slope(5, 3, 4, 2) == 1.0)
print(slope(1, 2, 3, 2) == 0.0)
print(slope(1, 2, 3, 3) == 0.5)
print(slope(2, 4, 1, 2) == 2.0)

def intercept(x1, y1, x2, y2):
    return y1-x1*slope(x1, y1, x2, y2)

print(intercept(1, 6, 3, 12) == 3.0)
print(intercept(6, 1, 1, 6) == 7.0)
print(intercept(4, 6, 12, 8) == 5.0)

# 14.
print('\nQ14')

# Function to return true if n is even and false otherwise

def is_even(n):
    return not n%2

print(is_even(3))
print(is_even(8))
print(is_even(0))

# 15.
print('\nQ15')

def is_odd(n):
    return n%2

# 16.
print('\nQ16')

def is_factor(f, n):
    return not n%f

print(is_factor(3, 12))
print(not is_factor(5, 12))
print(is_factor(7, 14))
print(not is_factor(8, 14))

# 17.
print('\nQ17')

def is_multiple(n, f):
    return is_factor(f, n)

print(is_multiple(12, 3))
print(is_multiple(12, 4))
print(not is_multiple(12, 5))

# 18.
print('\nQ18')

def f2c(t):
    return round((t-32)*5/9)

print(f2c(212) == 100)
print(f2c(32) == 0)
print(f2c(-40) == -40)
print(f2c(36) == 2)
print(f2c(37) == 3)
print(f2c(38) == 3)
print(f2c(39) == 4)

# Exercise on page 88

print('\nString exercises')


