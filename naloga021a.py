#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Izpišemo, za kakšen program gre
print("*"*64)
print("*"*5,"Karakteristike trikotnika","*"*5)
print("*"*64)

# Podamo stranice pravokotnika
a = input('Vnesite dolžino stranice a: ')
b = input('Vnesite dolžino stranice b: ')
c = input('Vnesite dolžino stranice c: ')

# definirajmo funkcijo, ki nam bo preverila vnesene stranice
def preveriStevilke(stevilka):
    try:
        stevilka = float(stevilka)
        return stevilka
    except:
        print(f"'{stevilka}' ni število.")
        quit()

print("-"*64)

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
a = preveriStevilke(a)
b = preveriStevilke(b)
c = preveriStevilke(c)

# uvedemo spremenljivko napaka tipa 'boolean', ki ima privzeto vrednost 'false'
napaka = False

# preverimo, če trikovnik s podanimi stranicami obstaja
if a + b > c:
    print(f"a + b > c: Pogoj JE izpolnjen -> {a} + {b} > {c}")
else:
    print(f"a + b > c: Pogoj NI izpolnjen -> {a} + {b} < {c}")
    napaka = True

if b + c > a:
    print(f"b + c > a: Pogoj JE izpolnjen -> {b} + {c} > {a}")
else:
    print(f"b + c > a: Pogoj NI izpolnjen -> {b} + {c} < {a}")
    napaka = True

if a + c > b:
    print(f"a + c > b: Pogoj JE izpolnjen -> {a} + {c} > {b}")
else:
    print(f"a + c > b: Pogoj NI izpolnjen -> {a} + {c} < {b}")
    napaka = True

print("-"*64)
if napaka == True:
    print(f"Trikotnik s podanimi stranicami {a}, {b} in {c} ne obstaja.")
else:
    obseg = a + b + c
    
    #polobseg
    s = obseg / 2

    # izračun površine po Heronovi formuli
    povrsina = (s*(s-a)*(s-b)*(s-c))**0.5

    # izpis
    print(f"Trikotnik s podanimi stranicami {a}, {b} in {c} ima obseg {obseg} in površino {povrsina}.")
