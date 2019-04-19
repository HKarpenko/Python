def kles(N):
    for i in range(2*N+1):
        if i<N:
            print(' '*i+'*'*(2*N+1-i*2))
        elif i==N:
            print(' '*i+'*')
        else:
            print(' '*(2*N-i)+'*'*(i*2-N*2+1))

kles(10)

