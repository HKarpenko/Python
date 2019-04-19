def schodki(n,k):
    for i in range(n):
        for j in range(k):
            print(' '*(n-i-1)*k+(i+1)*k*'*')

def cyfrowagranica(n):
    if len(str(n))==1:
        return n
    s=0
    for i in range(len(str(n))):
        s+=int(str(n)[i:i+1])
    return cyfrowagranica(s)

def najczestszagranica(a,b):
    granicy=[]
    for n in range(a,b+1):
        granicy.append(cyfrowagranica(n))
    czest=granicy.count(granicy[0])
    cel=granicy[0]
    for e in granicy:
        if czest<granicy.count(e):
            czest=granicy.count(e)
            cel=granicy[e]
    return cel

def pierwsz(licz):
    for i in range(2,licz):
        if licz%i==0:
            return 0
    return 1

def najwdziel(n):
    maxd=1
    for i in range(2,n//2+1):
        if n%i==0 and pierwsz(i):
            maxd=i
    return maxd

print(najwdziel(110))
        
