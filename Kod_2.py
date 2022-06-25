#считываем файл
with open('Spravochnik_2.txt','r', encoding="utf-8") as f:
    x = f.readlines()
    #print(x)


#убираем переносы
for j in range(0,len(x)):
    x[j] = x[j].strip()
print(x)

#Создаем новый список
new_spisok = []
for i in x:
    new_spisok.append(i.split("*"))
print(new_spisok)

#создаем словарь
spravocnik_2 = {}
for i in new_spisok:
    spravocnik_2[i[0] + " " + i[1]] = i[2]
#print(spravocnik_2)