def przekt(slowo):
    kod={}
    num=1
    for lit in slowo:
        if lit not in kod:
            kod[lit]=num
            num+=1
    for it in range(len(slowo)-1):
        print(str(kod[slowo[it]])+'-',end='')
    else:
        print(kod[slowo[-1:]],end=' ')
    print(slowo)

przekt('indianin')
            
            
