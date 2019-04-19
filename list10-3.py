from itertools import combinations,permutations

def policz(kod, slow1, slow2, wyn):
    a=''
    b=''
    c=''
    for lit in slow1:
        a+=kod[lit]
    for lit in slow2:
        b+=kod[lit]
    for lit in wyn:
        c+=kod[lit]
    if int(a)+int(b)==int(c):
        print(a+'+'+b+'='+c)
        return 1
    else:
        return 0

    
def zagad(nap):
    kod={}
    nap=nap.split()
    uniq=''
    for lit in nap[0]+nap[2]+nap[4]:
        if lit not in uniq:
            uniq+=lit
    if len(uniq)>10:
        return None
    for kmb in combinations('1234567890', len(uniq)):
        for per in permutations(kmb):
            kod={}
            kod = dict(zip(uniq, per))
            if kod[nap[0][0]]=='0' or kod[nap[2][0]]=='0' or kod[nap[4][0]]=='0':
                continue
            if policz(kod, nap[0], nap[2], nap[4]): 
                return kod
    else:
        return None


print(zagad("ciacho + ciacho = nadwaga"))
