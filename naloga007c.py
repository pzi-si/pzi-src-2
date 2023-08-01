#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Program, ki preveri, ali je podano število popoln kvadrat s kontrolami. """

# Izpišemo, za kakšen program gre
print("*"*53)
print("*"*5,"Program za preverjanje popolnih kvadratov","*"*5)
print("*"*53)

# Uvozimo potrebne Python module
import math

# Uporabnika pozovemo, da vpiše število, ki ga bomo preverili
stevilo = input("Vpišite število: ")

# Lepotni izpis
print("-"*53)

# Izpišemo število, ki ga je uporabnik vnesel
print(f"Število, ki ga preverjamo, je: {stevilo}")

# Lepotni izpis
print("="*53)

# Preverimo, ali je uporabnik vpisal število ali ne
try:
    # Spremenljivko število poskusimo pretvoriti v tip 'float'
    stevilo_stevilo = float(stevilo)
except:
    # Če pretvorba v tip 'float' ni uspešna, izpiši obvestilo in končaj program
    print("Podali ste niz znakov namesto števila.\nPreverjanje ni smiselno!")
    # Lepotni izpis
    print("-"*53)
    quit()


# Izračunamo koren podanega števila
koren = math.sqrt(stevilo_stevilo)

# Preverimo, če je izračunan koren tipa 'integer'
if koren.is_integer():
    # ker vemo, da je koren tipa integer, ga pretvorimo v ta tip
    koren = int(koren)
    # izpišemo besedilo
    print(f"Podano število {stevilo} je popoln kvadrat števila {koren}!")
else:
    # izpišemo obvestilo, da podano število ni popoln kvadrat 
    print(f"Podano število {stevilo} ni popoln kvadrat.")
# Lepotni izpis
print("-"*53)