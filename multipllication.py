def mul_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mul_numbers(n1,n2-1)
print(mul_numbers(5,4))