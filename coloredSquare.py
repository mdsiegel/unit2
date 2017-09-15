#Matthew Siegel
#9/13/17
#coloredSquare.py - make a colored square

from ggame import*
from random import randint
randnum = randint(1,1)
if randnum ==1:
    red = Color(0xff0000, 1)
    line = LineStyle(3,red)
    rectange = RectangleAsset(100,100,line,red)
elif randnum ==2:
    yellow = Color(0xffff00, 1)
    line = LineStyle(3,yellow)
    rectange = RectangleAsset(100,100,line,yellow)
elif randnum ==3:
    green = Color(0x00ff7f, 1)
    line = LineStyle(3,green)
    rectange = RectangleAsset(100,100,line,green)
elif randnum ==4:
    blue = Color(0x0000ff, 1)
    line = LineStyle(3,blue)
    rectange = RectangleAsset(100,100,line,blue)



