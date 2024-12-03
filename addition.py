'''
Author: Nandana Hasheed 
Date:3/12/2024
Program to add two positive numbers using function
'''
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
print(add_numbers(5,3))
