from turtle import fd, bk, rt, lt, up, down, speed, goto
import random
speed('fastest')
up()
goto(-600,0)
down()
lt(90)
wid=random.randint(5,10)
for i in range(100):
    het=random.randint(30,250)
    fd(het)
    rt(90)
    fd(wid)
    rt(90)
    fd(het)
    rt(90)
    fd(wid)
    up()
    bk(wid+3)
    rt(90)
    down()
