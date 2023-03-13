numberone = int(input('Enter First Number: '))
numbertwo = int(input('Enter Second Number: '))
print('Enter Operator (+,-,/,*):',end="")
ch = input()
result = 0
if ch == '+':
    print('Output for Addition is: ',numberone+numbertwo)
elif ch == '-':
    print('Output for Subtraction is: ',numberone-numbertwo)
elif ch == '*':
    print('Output for Multiplication is: ',numberone*numbertwo)
elif ch == '/':
    print('Output for Division is: ',numberone / numbertwo)
else:
    print('Invalid Operator...')