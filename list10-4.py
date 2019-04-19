from itertools import combinations
l_sum=[0]
def podzb(L):
    if len(L)==1:
        if L[0] not in l_sum:
            l_sum.append(L[0])
        return L[0]
    summ=0
    for co in combinations(L,len(L)-1):
        summ+=podzb(co)
    l_sum.append(summ)
    return summ

podzb([1,2,3])
print(l_sum)
