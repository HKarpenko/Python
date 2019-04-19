from turtle import *
import random
N=100
M=100
R=6
mapa = [ M * [0] for i in range(N)]
speed('fastest')
up()
goto(-300,300)
def kwadrat(R,kol):
    fillcolor(kol)
    begin_fill()
    for i in range(4):
        fd(R)
        rt(90)
    end_fill()

def pisz(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print (tab[i][j], end='')
        print()

def s_wys(a,b,mapa):
    summ=0
    il=0
    for i in range(3):
        for j in range(3):
            if 0<=a+1-i<=99 and 0<=b+1-j<=99:
                summ+=mapa[a+1-i][b+1-j]
                il+=1
    return summ//il

for i in range(1000):
    a = random.randrange(0,100)
    b = random.randrange(0,100)
    mapa[a][b] = random.randrange(3001,5001)
for i in range(100000):
    a = random.randrange(0,100)
    b = random.randrange(0,100)
    mapa[a][b]=s_wys(a,b,mapa)
for i in range(N):
    for j in range(M):
        if 0<=mapa[i][j]<=200:
            kolor='green'
        elif 200<mapa[i][j]<=400:
            kolor=(0.5, 1, 0)
        elif 400<mapa[i][j]<=700:
            kolor='yellow'
        elif 700<mapa[i][j]<=900:
            kolor='orange'
        elif 900<mapa[i][j]<=1200:
            kolor='red'
        else:
            kolor = (0.5, 0,0)
        kwadrat(R,kolor)
        fd(R)
    goto(-300,-R*(i+1)+300)
