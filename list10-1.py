def cesar(s,k):
    al="aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    al_k=al[len(al)-k:]+al[:len(al)-k]
    ces=dict(zip(al_k,al))
    wyn=''
    for lit in s:
        if lit not in ces:
            wyn+=lit
            continue
        wyn+=ces[lit]
    return wyn

print(cesar('ala ma kota',3))
