#Matthew Siegel
#9/13/17
#gradeCalculator.py - calculates your grade

grade = float(input('What is your grade? '))

if grade >= 90:
    print('You have an A')
elif grade >= 80:
    print('You have a B')
elif grade >=70:
    print('You have a C')
elif grade >=60:
    print('You have a D')
else:
    print('F')
