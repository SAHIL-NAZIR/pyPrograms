                                        # "Arithmetic operations in python"
    # numbers are taken as inputs
num1 = input('enter num1: ')
num2 = input('enter num2: ')
print('sum = ', float(num1) + float(num2))          # printing sum
print('difference = ', float(num1) - float(num2))   # printing difference
print('product = ', float(num1) * float(num2))      # printing product
print('ratio = ', float(num1) / float(num2))        # printing ratio
print(type(num1))
"""
    for line 9, output will be <class 'str'> because data type is not specified in line 3
    if we use num1 = float(input('enter num1: ')) instead of num1 = input('enter num1: ')
        then the output will be <class 'float'>
"""
