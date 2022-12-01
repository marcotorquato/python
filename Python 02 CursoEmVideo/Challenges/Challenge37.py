print('=====CHALLENGE 37=====')

num = int(input('Enter an integer: '))
print('''Choose one of the bases for conversion:
[ 1 ] convert to BINARY
[ 2 ] convert to OCTAL
[ 3 ] convert to HEZADECIMAL''')
option = int(input('You option is: '))
if option == 1:
    print('{} converted for BINARIO is {}'.format(num,(bin(num)[2:])))
elif option == 2:
    print('{} converted for OCTAL is {}'.format(num,(oct(num)[2:])))
elif option == 3:
    print('{} converted for EXADECIMAL is {}'.format(num, hex(num)[2:]))
else:
    print('Invalid')