from turtle import fd, bk, rt, lt, up, down, speed, fillcolor, begin_fill, end_fill, circle
speed('fastest')
up()
circle(100,190)
down()
R=100
for i in range(13):
    if i%3==0:
        fillcolor("yellow")
    elif i%3==1:
        fillcolor("green")
    else:
        fillcolor("blue")
    begin_fill()
    circle(R-i*6,360)
    end_fill()

