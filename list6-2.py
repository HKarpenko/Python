for slowo in open('s.txt'):
    odwr=''
    for i in range(len(slowo)):
        odwr+=slowo[len(slowo)-i-1]
    print(slowo,'-',odwr)
    if odwr in open('s.txt'):
        print(slowo,'-',odwr)
        
