from turtle import *
up()
goto(0,350)
down()
klr='yellow'
def kwadrat(bok):
    global klr
    fillcolor(klr)
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
    
def murek(s,bok):
  global klr
  for a in s:
     if a == 'f':
         kwadrat(bok)
         fd(bok)
     elif a == 'b':
         kwadrat(bok)
         fd(bok)         
     elif a == 'l':
         bk(bok)
         lt(90)
     elif a == 'r':
        rt(90)
        fd(bok)
     elif a == 'y':
        klr='yellow'
     elif a == 'g':
        klr='green'
     elif a == 'a':
        klr='aqua'
     elif a == 'k':
        klr='coral'


ht()

tracer(0,0) # szybkie rysowanie     
murek(4 * 'fgfafkfyfr',10)
up()
goto(0,0)
down()
for i in range(1,14):
    murek(i * 'fgfafkfy'+'r',10)
update() # uaktualnienie rysunku

