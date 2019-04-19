def only_once(L):
    for i in range(len(L)):
        L[i]=[L[i],i]
    L.sort()
    i=0
    while i != len(L)-1:
        if L[i][0]==L[i+1][0]:
            del L[i+1]
            i-=1
        i+=1
    L.sort(key=lambda i:i[1])
    for i in range(len(L)):
        L[i]=L[i][0]
    return L
    
print(only_once([1,2,3,1,2,3,8,2,2,2,9,9,4]))

