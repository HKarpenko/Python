def u2(n):
    if(n>=0):
        if(len(bin(n)[2:])>23):
            return 0
        print('0'*(24-len(bin(n)[2:]))+bin(n)[2:])
    else:
        if(len(bin(n)[3:])>23):
            return 0
        arr24=[]
        arr24=list('1'*(24-len(zamien(n)))+zamien(n))
        print(*arr24,sep='')
        buf=1
        n=23
        while(buf!=0):
            if n==0 and buf==1:                
                ['1']+arr24
            else:
                arr24[n]=str(int(arr24[n])+buf)
                buf=0
                if(arr24[n]=='2'):
                    buf=1
                    arr24[n]='0'
                n-=1
        print(*arr24,sep='')
                
def zamien(n):
    n=list(bin(abs(n))[2:])
    s=''
    for i in range(len(n)):
        if n[i]=='0':
            s+='1'
        else:
            s+='0'
    return s

u2(-1280000)
  

