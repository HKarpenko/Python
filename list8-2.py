def wslownik(s):
    slow = {}
    used=''
    for lit in range(len(s)):
        count=0
        if s[lit] not in used:
            used+=s[lit]
            count+=1
            for x in range(lit+1,len(s)):
                if s[lit]==s[x]:
                   count+=1
            slow[s[lit]]=str(count)
    return slow


def uklad(spraw,s_glow):
    s_spraw=wslownik(spraw)

    s_glow=wslownik(s_glow)
    for lit in spraw:
        if lit not in s_glow:
            return 0
        if int(s_spraw[lit])>int(s_glow[lit]):
            return 0
    return 1

print(uklad('kotka','lokomotywa'))


