#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Program, ki sešteje podani števili. """

# Izpišemo, za kakšen program gre
print("*"*40)
print("*"*5,"Program za seštevanje števil","*"*5)
print("*"*40)

# Podamo številki, ki ju seštevamo
sestevanec1 = input('Vnesite prvo število: ')

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
try:
    sestevanec1 = float(sestevanec1)
except:
    print(f"Prva podana vrednost ni število. Podali ste {sestevanec1}.")
    quit()

sestevanec2 = input('Vnesite drugo število: ')

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
try:
    sestevanec2 = float(sestevanec2)
except:
    print(f"Druga podana vrednost ni število. Podali ste {sestevanec2}.")
    quit()

# seštejemo števili
vsota = sestevanec1 + sestevanec2

# izpišemo vsoto
print(f"Rezultat: {sestevanec1} + {sestevanec2} = {vsota}")