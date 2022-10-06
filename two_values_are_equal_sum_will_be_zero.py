# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
c=int(input('Enter 3rd number: '))
if a==b or b==c or a==c:
    print('sum=0')
else:
    sum=a+b+c
    print(sum)