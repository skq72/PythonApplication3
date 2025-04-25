
from random import*
import random
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

    õiged=0
    sõnastik_random=list(sõnastik.items())
    random.shuffle(sõnastik_random)
    for eesti_sõna, vene_sõna in sõnastik_random:
        vastus=input(f"Tõlgi sõna {eesti_sõna}:").lower()
        if vastus==vene_sõna.lower():
            print("Õige vastus")
            õiged+=1
        else:
            print(f"Vale vastus!Õige oli:{vene_sõna}")
    print(f"\nSinu tulemus:{õiged}/{len(sõnastik)} õigesti.")











