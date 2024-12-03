'''
Author: Nandana Hasheed 
Date:3/12/2024
Python program to find the factorial of a number using function
'''
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
factorial(5)
