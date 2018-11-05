#!/urs/bin/env python3

# Function to print True if the number is prime number

def prime_num(n):
    indicator = 0
    for i in range(2, n//2+1):
        if n%i == 0:
            indicator = 1
            break
           
    if indicator == 1:
        print(str(n), "False")
    else:
        print(str(n), "True")


n = 56

if __name__ == '__main__':
    prime_num(n)



