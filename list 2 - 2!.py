def koperta(n):
    kwadr=[]
    for i in range(2*n+1):
        kwadr.append([])
        for j in range(2*n+1):
            if((i==0)|(j==0)|(i==2*n)|(j==2*n)|(i==j)|(i+j==2*n)):
                kwadr[i].append('*')
            else:
                kwadr[i].append(' ')
    for i in range(2*n+1):
        print(*kwadr[i])

koperta(10)
    
