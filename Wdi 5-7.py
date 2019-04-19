def makspot(n,m):
    k=1
    rez=2
    while rez<m:
        k=k+1
        rez=rez*2
    if n==2:
        return k+1
    l=1
    rez=2
    while rez<n:
        l=l+1
        rez=rez*2
    return k//l+1

print(makspot(2,63))
