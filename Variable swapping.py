                                            # Python program to swap two variables
x, y = input('x = '), input('y = ')
#Storing value of x in new variable s
s = x
#Assigning value of y to x
x = y
#Assigning value of x(stored in s) to y
y = s
#Printing swapped values
print("after swapping: \nx = ", x, "\ny = ", y)