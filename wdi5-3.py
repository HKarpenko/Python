def gcd(n,m):
    if m==0:
        return n
    if n<m:
        k=m
        m=n
        n=k
    licz=1
    while m>0:
        ilenp=n%2+m%2
        if ilenp==2:
            k=n%m
            n=m
            m=k
        elif ilenp==0:
            licz*=2
            n//=2
            m//=2
        elif n%2==0:
            n//=2
        else:
            m//=2
    return n*licz

print(gcd(42,28))
