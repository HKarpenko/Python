def koperta(n):
    for i in range(2*n+1):
        if((i==0)|(i==2*n)):
           print((2*n+1)*'*')
        elif(i<n):
            print('*',(i-1)*' ','*',(2*(n-i)-1)*' ','*',(i-1)*' ','*',sep="")
        elif(i==n):
            print('*',(i-1)*' ','*',(i-1)*' ','*',sep="")
        else:
            print('*',(2*n-i-1)*' ','*',(-1-2*(n-i))*' ','*',(2*n-i-1)*' ','*',sep="")
koperta(2)
