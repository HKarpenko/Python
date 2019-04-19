from duze_cyfry import daj_cyfre

def DLC(licz):
    cyf=[]
    for i in range(5):
        cyf.append([])
        for j in range(2*(len(str(licz))-1)+5*len(str(licz))):
                cyf[i].append(' ')
    for i in range(len(str(licz))):
         n=0
         for r in daj_cyfre(licz//(10**(len(str(licz))-i-1))-(10*(licz//(10**(len(str(licz))-i))))):
             cyf[n][i*7:i*7+5]=r;
             n+=1
    for i in range(5):
        print(*cyf[i],sep='')
        
DLC(2019)
