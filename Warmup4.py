#Matthew Siegel
#9/18/17
#Warmup4.py - finding if it is divisible by 7

num = int(input('Enter a number: '))

if num%7==0 or '7' in str(num) :
    print('Buzz')

else:
    print(num)