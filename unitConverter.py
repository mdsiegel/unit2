#Matthew Siegel
#9/13/17
#unitConverter.py - converts units to different units

numChose = int(input('1 for Km to miles, 2 for Kg to pounds, 3 for liters to gallons, 4 for celsius to fahrenheit'))

if numChose/1 ==1:
    Km = float(input('Enter a distance in Km: '))
    print('You have',Km*0.621371, 'miles')
if numChose/2 ==2:
    Kg = float(input('Enter Kg: '))
    print('You have',kg*0.621371, 'pounds')
if numChose/3 ==3:
    liters = float(input('Enter lites: '))
    print('You have',liters*0.621371, 'gallons')
if numChose/4 ==4:
    celsius = float(input('Enter a temp in celsius': '))
    print('You have',celsius*0.621371, 'fahrenheit')

