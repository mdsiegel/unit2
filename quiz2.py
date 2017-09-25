#Matthew Siegel
#9/25/17
#quiz2.py - How to do a quiz

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

if num1==num2:
    print('The numbers are the same')
elif num1>num2:
    print('The first number is bigger')
elif num1<num2:
    print('The second number is bigger')

if num1%3==0 and num2%3==0:
    print('They are both divisible by 3')
elif num1%3==0:
    print('The first number is divisible by 3')
elif num2%3==0:
    print('The second number is divisible by 3')

userProduct = int(input('Enter the product of the two numbers: '))
if userProduct == num1 * num2:
    print('Correct!')
else:
    print('Incorrect')