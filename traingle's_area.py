                                        # Area of triangle with python
print('Choose the type of triangle')
print(                                                      # Giving options
    '1. Equilateral traingle\n'
    '2. Isosceles Triangle\n'
    '3. Area of Triangle with Three Sides (Heron’s Formula)'
)
option = int(input())                                       # Taking option
if option == 1:                                             # For option 1
    '''Taking side of triangle'''
    side = float(input('side of triangle = '))
    # Calculating area
    area = pow(3, 1/2) / 4 * pow(side, 2)
    print('area = ', area, 'sq. units')
elif option == 2:                                             # For option 2
    '''Taking base & height of triangle'''
    base, height = float(input('base = ')), float(input('height = '))
    # Calculating area
    area = 1/2 * base * height
    print('area = ', area, 'sq. units')
elif option == 3:                                             # For option 3
    print('Enter three sides: ')
    '''Taking sides of triangle'''
    a, b, c = float(input('a = ')), float(input('b = ')), float(input('c = '))
    # Calculating Semi_Perimeter
    s = (a + b + c) / 2
    # Calculating area
    area = pow(s * (s-a) * (s-b) * (s-c), 1/2)
    print('area = ', area, 'sq. units')
else:                                             # For wrong option
    print('Invalid input!')
