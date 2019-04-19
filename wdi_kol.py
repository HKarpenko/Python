def slad(licz):
    sum=0
    while licz!=0:
        sum+=licz-licz//10*10
        licz=licz//10
    return sum

print(slad(1))

def maxslad(n,x):
    max1=slad(x[0])
    ind=1
    while slad(x[ind])==max1:
        ind+=1
        if ind>n-1:
            return 0
    else:
        if max1>slad(x[ind]):
            max2=slad(x[ind])
        else:
            max2=max1
            max1=slad(x[ind])
    for i in range(ind+1,n):
        if slad(x[i])>max2:
            if slad(x[i])>max1:
                max2=max1
                max1=slad(x[i])
            elif(slad(x[i])!=max1):
                max2=slad(x[i])
    return max2

def roz(n,x):
    for i in range(n-1):
        if slad(x[i])==slad(x[i+1]):
            return 0
    return 1

print(maxslad(5,[423, 123, 432, 131, 234]))
