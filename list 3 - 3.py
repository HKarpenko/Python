def usun_naw(s):
    for i in range(len(s)):
        if s[i]=='(':
            for j in range(i+1,len(s)):
                if s[j]==')':
                    s = s[0:i]+s[j+1:len(s)]
                    break
        if i == len(s)-1:
            break
    return(s)
print(usun_naw("Ala ma kota (perskiego)(!"))


