from math import sqrt

def wmap(naz):
    mapa=[]
    stan=[]
    odl=[]
    for wer in open(naz):
        mapa.append(wer[:-1])
    for w in range(len(mapa)):
        for p in range(len(mapa[w])):
            if mapa[w][p]=='#':
                stan.append((w,p))
    maks=0
    for e1 in range(len(stan)):
        for en in range(e1+1,len(stan)):
            odl.append((sqrt((stan[e1][0]-stan[en][0])**2+(stan[e1][1]-stan[en][1])**2),str(stan[e1])+'-'+str(stan[en])))
    print('max:',max(odl))
    s=0
    for el in odl:
        s+=el[0]
    s=s/len(odl)
    print('sred:',s)
    print('st/kw:',len(stan)/(len(mapa[0])*len(mapa)))


wmap('mapa.txt')
    
