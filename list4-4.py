def erast(n):
    checkl=[]
    for i in range(2,n+1):
        checkl.append(0)
    listp=[]
    for i in range(0,n-2):
        if checkl[i]==0:
            for j in range(i+1,n-1):
                if (j+2)%(i+2)==0:
                    checkl[j]=1
    for i in range(0,n-1):
        if checkl[i]==0:
            listp.append(i+2)
    return listp
def palindrom(a,b):
    pal=[]
    listp=erast(b)
    for i in range(4,len(listp)):
        if listp[i]>=a:
            for j in range(len(str(listp[i]))//2):
                if str(listp[i])[j]!=str(listp[i])[len(str(listp[i]))-j-1]:
                    break
            else:
                pal.append(listp[i])
    return pal
print(palindrom(1,31000))

