def date(m1,d1,m2,d2,m3,d3,m4,d4):
    if ((m1<m3 or (m1==m3 and d1<=d3)) and (m2>m3 or (m2==m3 and d2>=d3))) or ((m3<m1 or (m3==m1 and d3<=d1)) and (m4>m1 or (m4==m1 and d4>=d1))):
        print('wrong')

date(1,5,12,7,1,7,1,9)
