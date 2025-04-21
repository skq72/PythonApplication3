from operator import truediv
from random import*

andmed={}                                               #Добавляет список
andmed = {'nimi': 'Mari', 'vanus': 25, 'keel': 'eesti'} #Добавляет заполненый список
andmed = dict(nimi='Mari', vanus=25, keel='eesti')      #Добавляет заполненый список
print(andmed)
print(andmed["nimi"])                       #Показывает значение ключа по заданному ключу
print(andmed.get("nimi"))                   #Показывает значение ключа по заданному ключу
print(andmed.get("nimi_", "Ei ole sõnastikus"))
print(andmed.keys())                #Показывает все ключи в словаре
print(andmed.values())              #Показывает все значения в словаре
for k,v in andmed.items():          #Создаёт пару между значением и ключом
    print(k, v)
andmed["email"]="kirilladsmp-....@gmail.com" #Добавление в *список*
print(andmed)
andmed["prillid"]=True
print(andmed)
del andmed ["prillid"]
print(andmed)
andmed.update({"nimi":"Kati"})  #Поменять значение в *списке*
print(andmed)


read = ['Mis on Python?-programmeerimiskeel', 'Eesti pealinn?-Tallinn']
kus_vas = {}
for rida in read:
    kysimus, vastus = rida.split('-')
    kus_vas[kysimus.strip()] = vastus.strip()
print(kus_vas)
print(kus_vas["Eesti pealinn?"])    #Показывает значение ключа по заданному ключу

kysimused=list(kus_vas.keys())
while True:
    n=randint(0, len(read)-1)
    valitud_kysimus=kysimused[n]
    print(valitud_kysimus)
    vastus=input("Sisesta vastus:")
    if kus_vas[valitud_kysimus].lower()==vastus.lower():
        print("Õige vastus")
    elif kus_vas[valitud_kysimus].lower()==0:
        break
    else:
        print("Vale vastus")
