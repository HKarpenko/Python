def hanoi(wys,koll,kols,kolp):
    if wys>=1:
        hanoi(wys-1,koll,kolp,kols)
        moveDisk(koll,kols)
        hanoi(wys-1,kolp,kols,koll)



def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

hanoi(3,"A","B","C")
