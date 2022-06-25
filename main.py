import Kod
import user
#spravocnik ={"Иванов Иван": 563, "Ларин Роман": 866, "Саша Петров": 753, "Василиса Премудрая": 256, "Роман Орлов": 333}

#print(Kod.spravocnik)
spravocnik = Kod.spravocnik
#print(spravocnik)
#print("Введите имя: ")


try:
    q = user.a
    #a = str(input())
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
       if q == key[i][j]:
           x = key.index(key[i])
           #print(x)
           #print(telephone[x])
           print(key[i][0],key[i][1]," - ",telephone[x])


except:
     print("Такого абонента нет")






