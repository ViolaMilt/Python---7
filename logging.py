from datetime import datetime as dt
from time import time as t
import user

time = dt.now().strftime('%H:%M')
p = user.a

def obrashenie(p):
    with open('log.txt', 'a',encoding="utf-8") as file:
         file.writelines(str(time + p) + '\n')

c = obrashenie(p)

