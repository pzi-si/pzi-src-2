#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napiši program, ki od uporabnika bere števila, dokler uporabnik ne vpiše števila 0. Program naj sproti izpisuje največje, najmanjše in povprečje števil, vpisanih do sedaj.
"""

# Izpišemo, za kakšen program gre
print("*"*43)
print("*"*5,"Program za računanje statistike","*"*5)
print("*"*43)

# ustvarimo nov prazen seznam
stevila = []

while True:
    # uporabnika prosimo, naj vpisuje števila
    stevilo = input('Vnesi število: ')

    # če je vpisano število 0 naj se program prekine.
    if stevilo == "0":
        print("Pritisnili ste 0 in tako končali program.")
        quit()

    # preverimo, ali je uporabnik vnesel število
    try:
        stevilo = float(stevilo)
    except:
        print("Niste vnesli števila!")
        quit()
    
    stevila.append(stevilo)
    print(f"V seznamu so števila: {stevila}")
    print(f"Največje število = {max(stevila)}")
    print(f"Najmanjše število = {min(stevila)}")
    print(f"Povprečje števil v seznamu = {sum(stevila)/len(stevila)}")
    print("-"*40)
