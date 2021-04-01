                                        # solution of quadratic equation using python
print("Enter the values of a, b, c : ")
# Taking coefficients
a, b, c = float(input('a = ')), float(input('b = ')), float(input('c = '))
# Evaluating determinant
D = pow(b, 2) - 4 * a * c
if D == 0:                   #For unique real root
    # Evaluating and Printing roots
    print("Eqn has unique real root {:2.2f}".format(-b/2))
elif D > 0:                 #For distinct real roots
    # Evaluating roots
    x1, x2 = (-b + pow(D, 1/2)) / 2, (-b - pow(D, 1/2)) / 2
    # Printing roots
    print("Roots are %.2f" %x1, " & %.2f" %x2)
else:                       #For imaginary roots
    # Evaluating real part
    real = -b / 2
    # Evaluating imaginary part
    img = pow(-D, 1/2) / 2
    # Printing roots
    print("roots are \n\t(%.2f" % real, '+ %1.2f' %img, "i) and \n\t(%.2f" %real, '- %1.2f' %img, "i)")