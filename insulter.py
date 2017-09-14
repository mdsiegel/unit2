#Matthew Siegel
#9/13/17
#insulter.py - random insulter
from random import randint

name = input('Enter your name: ')
num = randint(1,5)
if num == 1:
    print(name, "You have no friends")
if num == 2:
    print(name, "You're so ugly that people run away screaming")
if num == 3:
    print(name, "You're so dumb that you try to put MnMs in alphabetical order")
if num == 4:
    print(name, "You're so dumb that you will starve to death in a super market")
if num == 5:
    print(name, "You have no friends")
