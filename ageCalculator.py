#Matthew Siegel
#9/18/17
#ageCalculator.py - Calculate the age

from datetime import date

year = int(input('Enter the year you were born: '))
month = int(input('Enter the month you were born: '))
day = int(input('Enter the day you were born: '))

yearsAlive = date.today().year - year
if month < date.today().month:
    print('You are',yearsAlive - 1,'years old')
elif month > date.today().month:
     print('You are',yearsAlive,'years old')
elif month == date.today().month:
    if day < date.today().day:
        print('You are',yearsAlive - 1,'years old')
    elif day > date.today().day:
        print('You are',yearsAlive ,'years old')
    elif day < date.today().day:
        print('You are',yearsAlive,'years old. HAPPY BIRTHDAY!!')

