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

# seštejemo števili
vsota = sestevanec1 + sestevanec2

# izpišemo vsoto
print(f"Rezultat: {sestevanec1} + {sestevanec2} = {vsota}")