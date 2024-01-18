#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Sestavi program, ki bo prebral tri realna števila, nato pa preveril, ali obstaja trikotnik s takimi dolžinami stranic. 
Če obstaja, naj program izračuna njegovo ploščino in obseg. 

Namig: Heronova formula: https://sl.wikipedia.org/wiki/Heronova_formula
"""

# Izpišemo, za kakšen program gre
print("*"*64)
print("*"*5,"Karakteristike trikotnika","*"*5)
print("*"*64)

# Podamo stranice pravokotnika
stranice = input('Vnesite dolžine stranic trikotnika, ki jih loči z vejico: ')

# Podan niz znakov pretvorimo v seznam
stranice = stranice.split(",")

# Preverimo, koliko delov ima seznam
if len(stranice) != 3:
    print("Podali ste več ali manj kot 3 stranice!")
    quit()

# če so tri stranice
a = stranice[0]
b = stranice[1]
c = stranice[2]

# definirajmo funkcijo, ki nam bo preverila vnešene stranice
def preveriStevilke(stevilka):
    try:
        stevilka = float(stevilka)
        return stevilka
    except:
        print("{} ni številka.")
        quit()

print("-"*90)

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
a = preveriStevilke(a)
b = preveriStevilke(b)
c = preveriStevilke(c)

# uvedemo spremenljivko napaka tipa 'boolean', ki ima privzeto vrednost 'false'
napaka = False

# preverimo, če trikovnik s podanimi stranicami obstaja
if a + b > c:
    print("a + b > c: Pogoj JE izpolnjen -> {} + {} > {}".format(a,b,c))
else:
    print("a + b > c: Pogoj NI izpolnjen -> {} + {} < {}".format(a,b,c))
    napaka = True

if b + c > a:
    print("b + c > a: Pogoj JE izpolnjen -> {} + {} > {}".format(b,c,a))
else:
    print("b + c > a: Pogoj NI izpolnjen -> {} + {} < {}".format(b,c,a))
    napaka = True

if a + c > b:
    print("a + c > b: Pogoj JE izpolnjen -> {} + {} > {}".format(a,c,b))
else:
    print("a + c > b: Pogoj NI izpolnjen -> {} + {} < {}".format(a,c,b))
    napaka = True

print("-"*90)
if napaka == True:
    print("Trikotnik s podanimi stranicami {}, {} in {} ne obstaja.".format(a,b,c))
else:
    obseg = a + b + c
    
    #polobseg
    s = obseg / 2

    # izračun površine po Heronovi formuli
    povrsina = (s*(s-a)*(s-b)*(s-c))**0.5

    # izpis
    print("Trikotnik s podanimi stranicami {}, {} in {} ima obseg {} in površino {}.".format(a,b,c,obseg,povrsina))
