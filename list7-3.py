slowa=[]
maksy=[]
for line in open('s.txt'):
    for x in line.split():
        count=0
        for lit in x:
            if lit.isalpha():
                count+=1
        slowa.append([count, x])
dlugm=max(slowa)[0]
for x in slowa:
    if x[0]==dlugm and x not in maksy:
        maksy.append(x)
maksy.sort(key=lambda i:i[1])
for s in maksy:
    print(s[1])
