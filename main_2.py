import Kod_2
import user
#spravocnik ={"Иванов Иван": 563, "Ларин Роман": 866, "Саша Петров": 753, "Василиса Премудрая": 256, "Роман Орлов": 333}

#print(Kod_2.spravocnik_2)
spravocnik = Kod_2.spravocnik_2
#print(spravocnik)
#print("Введите имя: ")


try:
    q2 = user.a
    #print(spravocnik[a])
    key = []
    for i in spravocnik.keys():
        key.append(i.split())
    #print(key)

    telephone = []
    for i in spravocnik.values():
        telephone.append(i)
    #print(telephone)

    for i in range(len(key)):
     for j in range(len(key[i])):
       if q2 == key[i][j]:
           x = key.index(key[i])
           #print(x)
           #print(telephone[x])
           print(key[i][0],key[i][1]," - ",telephone[x])


except:
     print("Такого абонента нет")




