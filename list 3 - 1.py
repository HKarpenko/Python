def liczp(licz):
        for i in range(2,licz):
            if(licz%i==0):
                return 0;
        return 1
for i in range(1,100001):
    if(liczp(i)):
        for j in range(len(str(i))-2):
            if(str(i)[j:j+3]=='777'):
                print(i)
                break
            
