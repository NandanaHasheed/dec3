'''
Author: Nandana Hasheed 
Date:3/12/2024
Python program to find the gcd of given number
'''
def gcd_number(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd_number(n2,n1%n2)
print(gcd_number(516,188))
