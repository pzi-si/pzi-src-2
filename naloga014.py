#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pravilno sklanjanje
"""

# uporabnika prosimo, naj vpiše število opravljenih izpitov
stevilo = input('Vnesi število opravljenih izpitov: ')

try:
    stevilo = int(stevilo)
except:
    print("Niste vnesli celega števila!")
    quit()

if stevilo%100 == 1:
    besedilo = "izpit"
elif stevilo%100 == 2:
    besedilo = "izpita"
elif stevilo%100 == 3 or stevilo%100 == 4:
    besedilo = "izpite"
else:
    besedilo = "izpitov"

print(f"Opravili ste {stevilo} {besedilo}.")