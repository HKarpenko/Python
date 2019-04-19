def Fun(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
def energy(n):
    ener=1
    while Fun(n)!=1:
        ener+=1
        n=Fun(n)
    return ener
def analiza_collatza(a,b):
    lcoll=[]
    for i in range(a,b+1):
        lcoll.append(energy(i))
    list.sort(lcoll)
    print(lcoll)
    print("Sriednie znacz: ", sum(lcoll)/len(lcoll))
    if len(lcoll)%2==1:
        print("Mediana: ", lcoll[len(lcoll)//2])
    else:
        print("Mediana: ", (lcoll[len(lcoll)//2-1]+lcoll[len(lcoll)//2])/2)
    print("Max energy: ", lcoll[0])
    print("Min energy: ", lcoll[len(lcoll)-1])
analiza_collatza(1,7)
