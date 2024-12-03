'''
Author: Nandana Hasheed 
Date:3/12/2024
Python program to find the fibonacci series of a number
'''
n=int(input("Enter a range"))
first_number=1
second_number=0
third_number=0
while(third_number<n):
    print(third_number,end=" ")
    third_number=first_number+second_number
    first_number=second_number
    second_number=third_number
