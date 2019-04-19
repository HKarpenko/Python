def z1a(n):
    if n%2==0:
        return n
    else:
        return -n
print(z1a(44))

def z1b(n):
    suma=0
    for i in range(1,n+1):
        if i%2==0:
            suma+=1/i
        else:
            suma+=-1/i
    return suma

print(z1b(3))

def z1c(n,x):
    suma=0
    xi=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            xi*=x
        suma+=xi*i
        xi=1
    return suma

print(z1c(2,3))

def NWD(a,b):
    if a<b:
        x = b
        b = a
        a = x
    while b>0:
        x = a%b
        a = b
        b = x
    return a

def ulamek(a,b):
    dziel=NWD(a,b)
    a=a/dziel
    b=b/dziel
    return a,b

def NWW(a,b):
    wyn=a*b/NWD(a,b)
    return wyn

print(NWD(14,21))    
print(NWW(68,34))    
print(ulamek(17,34))

def maxnwd(n,ll):
    mnwd=ll[0]
    for i in range(1,n):
        mnwd=NWD(mnwd,ll[i])
    return mnwd
print(maxnwd(3,[21,42,56]))

def bin_pal(n):
    s=[]
    i=0
    s.append(n%2)
    n=n//2
    while n>0:
        i+=1
        s.append(n%2)
        n=n//2
    for j in range((i+1)//2):
        if s[j]!=s[i-j]:
            return 0
    else:
        return 1
    
print(bin_pal(5))

def cyfrowy(n):
    ist=[]
    i=0
    l=n
    while k!=0:
        k//=10
        l+=1
    ist.append(n//((l-1)*10))
    for i in range(l):
        it = i*10
        if i==0:
            it =1
        for j in ist:
            if n//it-n//((l-i-1)*10)
            

print(cyfrowy(555))
        
