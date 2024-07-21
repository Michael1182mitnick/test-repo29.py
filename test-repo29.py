# Write a program to check if a given number is a prime number.
# using def function in python

def is_prime(num):
    # your code goes here
    # if number is greater than one then it's a prime number
    if num > 1:
        for x in range(2, num):
            if (num % 2) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")

prime_num = int(input("Enter any numbers: "))
is_prime(prime_num)