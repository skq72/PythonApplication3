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

print("Lisame uue sõna sõnastikku!")
uus_est = input("Sisesta sõna eesti keeles: ").strip().lower()
uus_rus = input("Sisesta sõna vene keeles: ").strip().lower()
sõnastik[uus_est]= uus_rus
print("Uus sõna on lisatud!")

sõna=input("Sisesta sõna parandamiseks:").lower()
for k in sõnastik:
    if sõna in sõnastik.keys():
        if k:
            print(f"Leitud {k} ")
            k=input("Uus eesti keeles: ").lower()
            k=input("Uus eesti keeles: ").lower()
            print("Sõna on parandatud")
            print(sõnastik)
        else:
            print("Sõna ei leitud")

           