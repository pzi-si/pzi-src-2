#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Program, ki za podano število pove, ali je praštevilo. """

# Uporabnika pozovemo, da vpiše število, ki ga preverjamo
stevilo = input("Vpišite število, za katerega vas zanima, ali gre za praštevilo: ")

# preverimo, ali je podano število tipa 'integer'
try:
    stevilo = int(stevilo)
except:
    print("Niste podali celega števila!")
    quit()

# uvedemo novo spremenljivko "napaka", ki ji določimo vrednost "False"
napaka = False

# za vsa števila od 2 do izbranega števila - 1 preverimo, ali je delitelj števila
for i in range(2,stevilo):
    # če je trenutno število i delitelj, spremenimo vrednost spremenljivke napaka
    if stevilo % i == 0:
        napaka = True

# če ima vrednost TRUE, potem izpišemo, da iskano število NI praštevilo
if napaka == True:
    print(f"Število {stevilo} NI praštevilo!")
else:
    print(f"Število {stevilo} JE praštevilo!")
