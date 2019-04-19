from itertools import permutations
def jednaWart(L):
    return L !=[] and all(x==L[0] for x in L)

print(jednaWart([]))

def najwroz(L):
    return max([abs(L[i]-L[i+1]) for i in range(len(L)-1)])

print(najwroz([1,2,5,12]))

def silnia(N):
    return eval(''.join([str(i)+'*' for i in range(1,N+1)])[:-1])

print(silnia(5))

def spk(N,K):
    return sum([x*x for x in range(1,N) if x%K==0])

print(spk(9,2))

def sorLeks(L):
    return sorted(list(map(str, L)))

print(sorLeks([1,4,55,222,9,10]))

def prefix(s,t):
    return any([ s==t[:i] for i in range(1,len(t)+1)])

print(prefix('pre','prefix'))

def drabina(L):
    return any([ L==([L[0]]+[L[1]])*i for i in range(1,len(L)//2+1) ])

print(drabina([1,2,1,2,1,2]))

def sdABC(L):
    return sum([ len(s) for s in L if all([ l in 'abc' for l in s]) ])

print(sdABC(['baba', 'ma', 'kota', 'a', 'ty?']))

def kub(N):
    return any([ N==a**3+b**3 for a in range(N) for b in range(N) ])

print(kub(27))

def rybymd(L):
    return [ True for pm in permutations(L) for e in range(len(pm)-1) if pm[e] in pm[e+1] ]

print(rybymd(['rekinisko', 'rekin', 'eki', 'megarekinisko', 'megarekiniskozilla']))

