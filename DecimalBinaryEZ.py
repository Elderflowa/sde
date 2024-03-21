integer = input("Enter an integer to convert to binary: ")

if integer.isdigit:
    integer = '{0:b}'.format(int(integer))
    print(integer)