def liczp(licz):
    for i in range(2,licz):
        if(licz%i==0):
            return 0;
    return 1
def trzy7(iter):
    for j in range(len(str(iter))-2):
        if(str(i)[j:j+3]=='777'):
            return 1
    return 0
        
for i in range(1,100001):
    if(trzy7(i) and liczp(i)):
         print(i)
            
