#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Program, ki sešteje podani števili. """


# Izpišemo, za kakšen program gre
print("*"*40)
print("*"*5,"Program za seštevanje števil","*"*5)
print("*"*40)

# Podamo številki, ki ju seštevamo
sestevanec1 = input('Vnesite prvo število: ')
sestevanec2 = input('Vnesite drugo število: ')

# spremenimo tip spremenljivke iz 'string' v 'float'
sestevanec1 = float(sestevanec1)
sestevanec2 = float(sestevanec2)

# seštejemo števili
vsota = sestevanec1 + sestevanec2

# izpišemo vsoto
print("Rezultat: "+str(sestevanec1)+" + "+str(sestevanec2)+" = "+str(vsota))