def gib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n==2:
        return 1
    return gib(n-1)+gib(n-2)+gib(n-3)

def fTrec(n,m):
    if n==0:
        return m
    if m==0:
        return n
    return fTrec(n-1,m)+2*fTrec(n,m-1)

def minpot(n,m):
    k=0
    rez=0
    while rez<m:
        k+=1
        a=n
        b=k
        rez=1
        while b>0:
            if b%2:
                rez=rez*a
            b//=2
            a*=a
    return k



    
