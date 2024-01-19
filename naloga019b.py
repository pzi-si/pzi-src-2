#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Izpišemo, za kakšen program gre
print("*"*60)
print("*"*5,"Program za izračun največjega skupnega delitelja","*"*5)
print("*"*60)

# definirajmo funkcijo, ki nam bo preverila, če sta vnešeni številki celi
def preveriStevilke(stevilka):
    try:
        stevilka = int(stevilka)
        return stevilka
    except:
        print(f"'{stevilka}' ni številka.")
        quit()

# Pozovemo uporabnika, naj poda števila
stevila = input("Podajte števila (ločite jih z vejico): ")

# sestavimo seznam s števili
stevila_string = stevila.split(",")

# uvedemo seznam stevila
stevila = []

# preverimo števila in jih dodamo v seznam, če ni napake
for i in stevila_string:
    i = preveriStevilke(i.replace(" ",""))
    stevila.append(i)

# izpišemo vnešena števila
print(f"Vnesli ste števila: {stevila}")
print("-"*60)

i = 1
while i < len(stevila):
    if i == 1:
        a,b = stevila[i],stevila[i-1]
    else:
        a,b = stevila[i],delitelj
    a_original,b_original = a,b

    print(f"Preglejujem številki {a} in {b}.")
    # Evklidov algoritem
    while b:
        n = math.floor(a/b)
        print(f"{a} = {n} * {b} + {a%b}")
        a,b=b,a%b
    delitelj = a
    print(f"Največji skupni delitelj števil {a_original} in {b_original} je {delitelj}.")
    print("-"*60)
    i += 1

print(f"Največji skupni delitelj števil {', '.join(stevila_string)} je {delitelj}.")