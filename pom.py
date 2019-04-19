def podzial(l,p,a):
    x=a[l]
    i=l
    j=p
    while i<j:
        while a[j]>x: j-=1
        while a[i]<x: i+=1
        if i<j:
            y=a[j]
            a[j]=a[i]
            a[i]=y
            i+=1
            j-=1
    return j

print(podzial(0,3,[3,1,4,2]))
