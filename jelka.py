import random
from turtle import fd, bk, rt, lt, up, down, speed, goto, circle, fillcolor, begin_fill, end_fill, reset
speed('fastest')
def segment(roz,bomb):
    fillcolor('green')
    begin_fill()
    for i in range(3):
        fd(roz)
        lt(120)
    end_fill()
    while bomb!=0:
        for i in range(3):
            for j in range(10):
                fd(roz/10)
                if random.randrange(10)==7:
                    up()
                    lt(90)
                    down()
                    bombka()
                    rt(90)
                    bomb-=1
                    if bomb==0:
                        lt(120*i)
                        break
            if bomb==0:
                lt(120*i)
                break  
            lt(120)          


def bombka():
    kolor=random.choice(['red','orange','yellow'])
    rozb=random.randrange(5,16)
    fillcolor(kolor)
    begin_fill()
    circle(rozb,360)           
    end_fill()

segment(300,30)
up()
goto(0,0)
goto(50,125)
down()
segment(200,20)
up()
goto(0,0)
goto(100,225)
down()
segment(100,10)

