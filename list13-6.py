from itertools import permutations
def zrob_tytul(s):
    return ' '.join([ l[0].upper()+l[1:] for l in s.split() ])

print(zrob_tytul("ala ma kota i psa"))

def suma_jednocyfrowych(L):
    return sum( [ el for el in L if len(str(el))==1 ] )

print(suma_jednocyfrowych([1,2,3,55,4534,6787]))

def same_palindromy(L):
    return all([ el[:len(el)//2]==(el[len(el)-len(el)//2:])[::-1] for el in L ])

print(same_palindromy(['ala', 'ama', 'atota', 'i', 'assa']))

def namiotowa(L):
    return any( [ L[:s]==sorted(L[:s]) and (L[s:])[::-1]==sorted(L[s:]) for s in range(len(L)+1) ] )

print(namiotowa([1,2,4,1]))

def maksymalna_liczba_w_tekscie(s):
    return max([ int(''.join([ zn for zn in sl if zn.isdigit()])) for sl in s.split() ])

print(maksymalna_liczba_w_tekscie('123 11 krowa333byk'))

def wydluzalne(L):
    return any( [ all([ per[i] in per[i+1] for i in range(len(per)-1) ]) for per in permutations(L) ])

print(wydluzalne(['bc', 'a', 'ab']))
