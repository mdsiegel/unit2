#Matthew Siegel
#9/13/17
#fortuneTeller.py - Tells 8 different fortunes

color = (input('Pick red or blue: ')).upper()
num = int(input('Pick a number from 1-4'))

if color == 'BLUE' and num == 1:
    print('You will flunk out of school')
if color == 'BLUE' and num == 2:
    print('You will get straight As')
if color == 'BLUE' and num == 3:
    print('You will get eaten by a shark')
if color == 'BLUE' and num == 4:
    print('The red sox will win the world series')
if color == 'RED' and num == 1:
    print('You are in computer programing')
if color == 'RED' and num == 2:
    print('Look behind you')
if color == 'RED' and num == 3:
    print('Lock your doors tonight')
if color == 'RED' and num == 4:
    print('You will win a bear')
