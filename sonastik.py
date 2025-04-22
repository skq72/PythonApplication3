
from random import*

sõnastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

sõnastik2={
    'собака': 'koer',
    'кошка': 'kass',
    'дом': 'maja',
    'машина': 'auto',
    'солнце': 'päike'
}

def tervistus():
    print("Tere tulemast eesti-vene sõnastikku!")
    
def munuu():
    print("Valikud:")
    print("1 - Tõlgimine")
    print("2 - Lisa uus sõna")
    print("3 - Paranda sõna")
    print("4 - Testi teadmisi")
    print("5 - Välju")
    
def tõlk(sõnastik,sõnastik2):
    tõlg=input("Millest millise keeleni kui est->rus siis sisesta (er) aga kui tahad rus->est siis sisesta (re) :  ")
    if tõlg=="er":
        print(sõnastik.keys())
        sõna_e=input("Vali üks ja sisesta:  ")
        print(sõnastik.get(sõna_e))
    elif tõlg=="re":
       print(sõnastik2.keys())
       sõna_r=input("Vali üks ja sisesta:  ")
       print(sõnastik2.get(sõna_r))
    else:
        print("On vaja kirjutada (er) VÕI (re)!!!!")
def uusõna(sõnastik):
    print("Lisame uue sõna sõnastikku!")
    uus_est = input("Sisesta sõna eesti keeles: ").strip().lower()
    uus_rus = input("Sisesta sõna vene keeles: ").strip().lower()
    sõnastik[uus_est]= uus_rus
    print("Uus sõna on lisatud!")
def parandsõna(sõnastik):
    est=input("Sisesta sõna eesti keeles milline sa tahad muuta: ")
    if est in sõnastik:
       uus_vene=input(f"Praegune tõlge on {sõnastik[est]}. Sisesta uus vene tõlge: " ).strip()
       sõnastik[est]=uus_vene
       print("Tõlge on muudatud")
       print(sõnastik)
             
def test(sõnastik):

    kus_vas = sõnastik
    print(kus_vas["koer"])   
    kysimused=list(kus_vas.keys())
    while True:
        n=randint(0, len(sõnastik)-1)
        valitud_kysimus=kysimused[n]
        print(valitud_kysimus)
        vastus=input("Sisesta vastus:")
        if kus_vas[valitud_kysimus].lower()==vastus.lower():
            print("Õige vastus")
        elif kus_vas[valitud_kysimus].lower()==0:
            break
        else:
            print("Vale vastus")

# -----------
#     print(kus_vas["kass"])   
#     kysimused=list(kus_vas.keys())
#     while True:
#         n=randint(1, len(sõnastik)0)
#         valitud_kysimus=kysimused[n]
#         print(valitud_kysimus)
#         vastus=input("Sisesta vastus:")
#         if kus_vas[valitud_kysimus].lower()==vastus.lower():
#             print("Õige vastus")
#         elif kus_vas[valitud_kysimus].lower()==1:
#             break
#         else:
#             print("Vale vastus")









