#считываем файл
with open('Spravochnik.txt','r', encoding="utf-8") as f:
    x = f.readlines()


#убираем переносы
for j in range(0,len(x)):
    x[j] = x[j].strip()

#создаем словарь
spravocnik = {}
for i in range(0,len(x)-2,3):
    spravocnik[x[i] + " " + x[i+1]] = x[i+2]

#print(spravocnik)
