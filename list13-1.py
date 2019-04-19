from random import randrange

def kratka(N):
    liczby=[]
    for i in range(N*N):
        liczby.append(randrange(10))
    print(liczby)
    for i in range(3*N+1):
        if i%3==0:
            ind=i//3
            print((N*3+1)*'#')
        else:
            for j in range(N):
                print('#'+2*str(liczby[j+N*ind]),end='')
            print('#')
        


kratka(5)
