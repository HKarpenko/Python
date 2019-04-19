from turtle import fd, bk, rt, lt, goto, speed, pencolor, pu, pd, fillcolor, begin_fill, end_fill
import random
pu()
speed('fastest')
goto(-500,0)
N=80
a=15
def kwadrat(b):
    for i in range(4):
        fd(b)
        rt(90)

def zmiesz(p, k1, k2):
    r1, g1, b1 = k1
    r2, g2, b2 = k2
    r3 = p*r1+(1-p)*r2
    g3 = p*g1+(1-p)*g2
    b3 = p*b1+(1-p)*b2
    return r3,g3,b3

red=(0,1.0,0)
green=(0,0,1.0)
for i in range(N):
    fillcolor(zmiesz(i/(N-1),red,green))
    begin_fill()
    kwadrat(a)
    end_fill()
    fd(a)

    
    
    
