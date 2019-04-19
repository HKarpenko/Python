from turtle import fd, bk, rt, lt, up, down, tracer, goto, speed, fillcolor, begin_fill, end_fill
tracer(0,1)
R=10
def rys(rgb):
    a=rgb[0]/255
    b=rgb[1]/255
    c=rgb[2]/255
    fillcolor(a,b,c)
    up()
    begin_fill()
    for i in range(4):
        fd(R)
        rt(90)
    fd(R)
    down()
    end_fill()
    
count=0  
for line in open('obraz.txt'):
    uz=0
    count+=1
    for s in range(len(line)):
        if line[s]==')':
            obr=eval(line[uz:s+1])
            rys(obr)
            uz=s+1
        if s==len(line)-1:
            up()
            goto(0,-count*R)
            down()
            
            
    




 

   
    
