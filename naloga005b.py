#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Program za računanje ploščine in obsega pravokotnika. """

# Izpišemo, za kakšen program gre
print("*"*64)
print("*"*5,"Program za računanje ploščine in obsega pravokotnika","*"*5)
print("*"*64)

# Podamo stranici pravokotnika
stranicaA = input('Vnesite dolžino stranice a: ')

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
try:
    stranicaA = float(stranicaA)
except:
    print(f"Podali ste '{stranicaA}', kar ni število.")
    quit()

stranicaB = input('Vnesite dolžino stranice b: ')

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
try:
    stranicaB = float(stranicaB)
except:
    print(f"Podali ste '{stranicaB}', kar ni število.")
    quit()

# izračun obsega in ploščine
obseg = 2*stranicaA + 2*stranicaB
ploscina = stranicaA * stranicaB

# izpišemo ploščino in obseg
print(f"Ploščina pravokotnika s stranicama {stranicaA} in {stranicaB} je {ploscina}.")
print(f"Obseg pravokotnika s stranicama {stranicaA} in {stranicaB} je {obseg}.")