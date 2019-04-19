def szybpot(a,b):
    rez=1
    mnoz=0
    while b>0:
        if b%2==1:
            rez*=a
        b//=2
        a*=a
    return rez

def szybpot1(a,b):
    rez=1
    mnoz=0
    while b>0:
        if b%2==1:
            rez*=a
            mnoz+=1
        b//=2
        a*=a
        mnoz+=1
    return mnoz, rez

def mnozenia(k):
    print("max: ", szybpot(2,k+1)-1, szybpot1(5,szybpot(2,k+1)-1))

mnozenia(10)
