#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Izpišemo, za kakšen program gre
print("*"*60)
print("*"*5,"Program za izračun največjega skupnega delitelja","*"*5)
print("*"*60)

# definirajmo funkcijo, ki nam bo preverila, če sta vnešeni števili celi
def preveriStevilke(stevilka):
    try:
        stevilka = int(stevilka)
        return stevilka
    except:
        print(f"'{stevilka}' ni številka.")
        quit()

# Pozovemo uporabnika, naj poda dve celi števili
stevilo1 = input("Podajte prvo celo število: ")
# preverimo števili
stevilo1 = preveriStevilke(stevilo1)

stevilo2 = input("Podajte drugo celo število: ")
stevilo2 = preveriStevilke(stevilo2)

print("-"*60)

# določimo spremenljivki a in b
a,b = stevilo1,stevilo2

# Evklidov algoritem
while b:
    n = math.floor(a/b)
    print(f"{a} = {n} * {b} + {a%b}")
    a,b=b,a%b
print(f"Največji delitelj števil {stevilo1} in {stevilo2} je {a}.")