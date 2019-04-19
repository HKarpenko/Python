from turtle import *
speed('fastest')
def rek_kwadr(n):
    if n == 128:
        kolor='black'
    elif n == 64:
        kolor='blue'
    elif n == 32:
        kolor='yellow'
    elif n == 16:
        kolor='green'
    if n<=8:
        kolor='red'
        up()
        fd(n/2)
        down()
        fillcolor(kolor)
        begin_fill()
        lt(90)
        fd(n/2)
        lt(90)
        for i in range(3):
            fd(n)
            lt(90)
        fd(n/2)
        lt(90)
        end_fill()
        up()
        fd(n/2)
        down()
        lt(180)
    else:
        up()
        fd(n/2)
        down()
        fillcolor(kolor)
        begin_fill()
        lt(90)
        fd(n/2)
        lt(90)
        for i in range(3):
            fd(n)
            lt(90)
        fd(n/2)
        end_fill()
        rt(90)
        up()
        fd(n/4)
        down()
        rek_kwadr(n/2)
        up()
        bk(3*n/2)
        down()
        rek_kwadr(n/2)
        up()
        fd(3*n/4)
        down()
        lt(90)
        up()
        fd(3*n/4)
        down()
        rt(90)
        rek_kwadr(n/2)
        lt(90)
        up()
        bk(3*n/2)
        down()
        rt(90)
        rek_kwadr(n/2)
        lt(90)
        up()
        fd(3*n/4)
        down()
        rt(90)
        
rek_kwadr(128)
