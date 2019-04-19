def podziel(s):
    slowa=[]
    count=0
    for i in range(len(s)):
        if s[i] == ' ' and s[i-1]!=' ':
            slowa.append(s[i-count:i])
            count=0
        if s[i] != ' ':
            count+=1
    return slowa

print(podziel("   Alahlrd hfgndf  ma    kota    "))


        
        
    
