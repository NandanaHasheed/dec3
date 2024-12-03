'''
Author: Nandana Hasheed 
Date:3/12/2024
Python program to find the fibonacci series of number
'''
def generate_fibonacci(n):
    sequence=[]
    first_number,second_number=0,1
    for _ in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
print(generate_fibonacci(10))
