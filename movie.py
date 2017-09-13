#Matthew Siegel
#9/13/17
#movie.py - checks what movies you can watch

age = int(input('Enter your age: '))

if age >=17:
    print('You can watch R movies')
elif age >=13:
    print('You can watch PG-13')
else:
    print('You can watch PG ratings')
