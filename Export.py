import Kod
with open('Export Spravochnik.txt','w', encoding="utf-8") as ex:
    itog = Kod.spravocnik
    for key, value in itog.items():
        ex.write(f'{key}, {value}\n')


    with open('text.txt', 'w') as file:
        for key, value in itog.items():
            file.write(f'{key} - {value}\n')


