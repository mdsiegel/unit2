#Matthew Siegel
#9/18/17
#quadradic.py - solves quadradics

print('ax^2 + bx + c = 0')


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (b**2 - 4*(a)*(c)) >= 0:
    x1 = (-b + (b**2 - 4*(a)*(c))**.5)/2*(a)
    x2 = (-b - (b**2 - 4*(a)*(c))**.5)/2*(a)
    if x1 != x2:
        print('x =',x1, 'or x =',x2 )
    else:
        print('x =',x1)
else:
    x1 = (-b/(2*a))
    i1 = (-1*(b**2 - 4*(a)*(c)))**.5
    i2 = -((-1*(b**2 - 4*(a)*(c)))**.5)
    print('x =',x1,'+',i1, 'i', 'or x =',x1,'+',i2, 'i' )
  
    


