'''
Author: Nandana Hasheed 
Date:3/12/2024
Python program to find the factorial of number
'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
factorial(5)
