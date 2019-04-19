from losowanie_fragmentow import losuj_fragment
def losuj_haslo(n):
    hasl = ''
    while len(hasl) != n:
        hasl = hasl + losuj_fragment()
        if len(hasl)>n:
            hasl = ''
    return hasl
for i in range(10):
    print('n = 8 haslo: ',losuj_haslo(8))
for i in range(10):
    print('n = 10 haslo:',losuj_haslo(10))
