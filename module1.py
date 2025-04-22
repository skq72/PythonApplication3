from sonastik import *
tervistus()
while True:
    munuu()
    valik = input("\nSisesta oma valik 1-5 :  ")
    if valik == "1":
        tõlk(sõnastik,sõnastik2)
    elif valik == "2":
        uusõna(sõnastik)
    elif valik == "3":
        parandsõna(sõnastik)
    elif valik == "4":
        test(sõnastik)
    elif valik =="5":
        break
    else:
        print("Viga! Proovi veel kord")