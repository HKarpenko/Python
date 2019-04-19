from turtle import fd, bk, rt, lt, up, down, speed, goto, color, fillcolor, begin_fill, end_fill
speed('fastest')

def mieszanka(a, kolor1, kolor2):
    r1, g1, b1 = kolor1
    r2, g2, b2 = kolor2
    r3 = a * r1 + (1-a) * r2
    g3 = a * g1 + (1-a) * g2
    b3 = a * b1 + (1-a) * b2
    return r3, g3, b3
def kwadr(a,kl):
    fillcolor(kl)
    begin_fill()
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()
    fd(a)
K1 = (0.95, 0, 0.86)
K2 = (0.9, 0.9, 0)
num=0
for i in range(2,20):
    for j in range(i):
        num+=1
        a=num/200
        kwadr(15,mieszanka(a, K1, K2))
    rt(90)

