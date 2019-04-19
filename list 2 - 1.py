def szachownica(n,k):
    for i in range(n):
        for j in range(k):
            for z in range(n):
                print(k*' ',k*'#', end='')
            print('')
        for j in range(k):
            for z in range(n):
                print(k*'#',k*' ', end='')
            print('')
szachownica(4,1)

