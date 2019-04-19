import time
from math import sqrt
sdm=8
cyfr=10
sczet=0
def prm(licz):
    for i in range(2,int(sqrt(licz))+1):
        if(licz%i==0):
            return 0;
    return 1
t0=time.time()
for i in range(cyfr-sdm+1):
    if i==0:
        for j in range(0,int('1'+(cyfr-sdm)*'0')):
            s_itl='0'*(cyfr-sdm-len(str(j)))+str(j)
            sgen=''
            sgen='7'*sdm+s_itl
            if prm(int(sgen)):
                sczet+=1
                print(int(sgen))
    else:  
        for j in range(int('1'+(cyfr-sdm-1)*'0'),int('1'+(cyfr-sdm)*'0')):
            s_itl=str(j)
            sgen=''
            sgen=s_itl[0:i]+('7'*sdm)+(s_itl[i:len(s_itl)])
            if prm(int(sgen)):
                sczet+=1
                print(int(sgen))
t1=time.time()-t0
print(sczet)
print(t1)       
        
