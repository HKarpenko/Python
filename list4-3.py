import random
def randperm(n):
    wyn=[]
    los=list(range(n))
    for i in range(n):
        num=random.randint(0,n-i-1)
        wyn.append(los[num])
        los[n-i-1],los[num] = los[num],los[n-i-1]
    return wyn
print(randperm(10**2))
        
