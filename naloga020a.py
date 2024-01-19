#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("*********************************")
print("***** Igra: ugani številko! *****")
print("*********************************")

# vključim modul random, da bom lahko izbral naključen integer
import random

# izberem iskano številko
iskanaStevilka = random.randint(0,100)

steviloPoskusov = 0

#nastavim začetno število na vrednost, ki zagotovo ni enaka iskani
stevilka = -1

while stevilka != iskanaStevilka:
    stevilka = input("Ugani številko med 0 in 100: ")
    steviloPoskusov += 1
    if stevilka.isnumeric(): 
        stevilka = int(stevilka)
        if stevilka != iskanaStevilka:
            print(f"Poskus št. {steviloPoskusov}. {stevilka} ni prava številka.")
            print(f"Poskusi znova!")
        elif stevilka == iskanaStevilka:
            print(f"Bravo! V {steviloPoskusov}. poskusu si uganil številko {stevilka}!")
            print(f"Igra je končana!")
    else:
        print(f"Poskus št. {steviloPoskusov}. Vnesel si '{stevilka}', kar ni cela številka.")
        print(f"Poskusi znova!")

