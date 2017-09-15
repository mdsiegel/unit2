#Matthew Siegel
#9/13/17
#adventure.py - like the adventure game

print('You are going on a fun hike. All of a sudden, you see a strange man in the distnace. Do you run away?')
if input('yes or no') == 'yes':
    print('You look behind you and see him chasing you. Do you keep running or try to talk with him?')
    if input('run or talk') == 'run':
        print('He comes up behind you and eats your face off. THE END')
    else:
        print('You go up to talk with him. It turns out though that he is a zombie. There is a rock next to you. Do you throw it?')
        if input('yes or no')=='yes':
            if input('Do you through it at his head or body') == 'head':
                print('You kill the zombie. YAY')
                
            