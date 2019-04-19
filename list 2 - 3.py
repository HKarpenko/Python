def kolko(n):
    kol=[]
    for i in range(n//2):
        kol.append([])
        for j in range(n):
                kol[i].append('#')
    if(n<=5):
        kol[0][0]=kol[0][n-1]=' '
    elif(n<10): 
        kol[0][0:2]=kol[0][n-2:n]='  '
        kol[1][0]=kol[1][n-1]=' '
    elif(n<15):
        kol[0][0:4]=kol[0][n-4:n]='    '
        kol[1][0:2]=kol[1][n-2:n]='  '
        kol[2][0]=kol[3][0]=kol[2][n-1]=kol[3][n-1]=' '
    elif(n<20):
        kol[0][0:5]=kol[0][n-5:n]='     '
        kol[1][0:4]=kol[1][n-4:n]='    '
        kol[2][0:2]=kol[2][n-2:n]='  '
        kol[3][0]=kol[4][0]=kol[4][n-1]=kol[3][n-1]=' '
    elif(n<25):
        kol[0][0:6]=kol[0][n-6:n]='      '
        kol[1][0:4]=kol[1][n-4:n]=kol[2][0:4]=kol[2][n-4:n]='    '
        kol[3][0:2]=kol[3][n-2:n]=kol[4][0:2]=kol[4][n-2:n]='  '
        kol[5][0]=kol[6][0]=kol[6][n-1]=kol[5][n-1]=kol[7][0]=kol[7][n-1]=' '
    else:
        kol[0][0:7]=kol[0][n-7:n]='       '
        kol[1][0:5]=kol[1][n-5:n]=kol[2][0:5]=kol[2][n-5:n]='     '
        kol[3][0:3]=kol[3][n-3:n]=kol[4][0:3]=kol[4][n-3:n]='   '
        kol[5][0:2]=kol[5][n-2:n]=kol[6][0:2]=kol[6][n-2:n]='  '
        kol[7][0]=kol[8][0]=kol[8][n-1]=kol[7][n-1]=kol[9][0]=kol[9][n-1]=' '
    return kol

def balwanek(n1,n2,n3):
    max=n1
    if(n2>max):max=n2
    if(n3>max):max=n3
    for i in range(n1//2):
        print((max-n1)//2*' ',end='')
        print(*kolko(n1)[i],sep='')
    print((max-n1)//2*' ',end='')
    print(n1*'#')
    for i in range(n1//2):
        print((max-n1)//2*' ',end='')
        print(*kolko(n1)[n1//2-i-1],sep='')
    for i in range(n2//2):
        print((max-n2)//2*' ',end='')
        print(*kolko(n2)[i],sep='')
    print((max-n2)//2*' ',end='')
    print(n2*'#')
    for i in range(n2//2):
        print((max-n2)//2*' ',end='')
        print(*kolko(n2)[n2//2-i-1],sep='')
    for i in range(n3//2):
        print((max-n3)//2*' ',end='')
        print(*kolko(n3)[i],sep='')
    print((max-n3)//2*' ',end='')
    print(n3*'#')
    for i in range(n3//2):
        print((max-n3)//2*' ',end='')
        print(*kolko(n3)[n3//2-i-1],sep='')
balwanek(9,9,9)    
    
