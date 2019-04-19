def sil(n): #Возвращает факториал
    wyn=1
    for i in range(n):
        wyn = wyn*(i+1)
    return wyn
def cyfra(): #Подбирает правильное окончание
    if(len(str(sil(i)))%10==1):
        return "cyfrę"
    elif(0<len(str(sil(i)))%10<5):
        return "cyfry"
    else:
        return "cyfr"
for i in range(100):
    print(i,'! ma ',len(str(sil(i))),cyfra())
    
    

    
