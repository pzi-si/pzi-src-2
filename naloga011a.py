#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napiši program, ki izpiše prvih _X_ členov Fibonaccijevega zaporedja. Število _X_ na poziv vnese uporabnik.
"""

# Uporabnika pozovemo, da vpiše število, koliko členov Fibonaccijevega zaporedja naj prikažemo
stevilo = input("Vpišite, koliko členov Fibonaccijevega zaporedja vas zanima: ")

# preverimo, ali je podano število tipa 'integer'
try:
    stevilo = int(stevilo)
except:
    print("Niste podali celega števila!")
    quit()

#ker moramo vedno poznati dve števili zaporedja, uvedemo dve novi neznanki
stevilo_ena = 1
stevilo_dva = 1
# za vsa števila od 1 do izbranega števila + 1 izračunamo in izpišemo
for i in range(1,stevilo+1):
    print(stevilo_ena)
    # uvesti moramo novo spremeljivko, da si začasno zapomni vrednost spremenljivke stevilo_ena
    stevilo_nic = stevilo_ena
    stevilo_ena = stevilo_dva
    stevilo_dva = stevilo_nic+stevilo_dva
