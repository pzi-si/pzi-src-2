#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("*"*43)
print("*** Iskanje deliteljev podanega števila ***")
print("*"*43)

# Uporabnika pozovemo, da vpiše število, katerega delitelje bomo iskali
stevilo = input("Vpišite število, za katerega želite poiskati vse delitelje: ")

# preverimo, ali je podano število tipa 'integer'
try:
    stevilo = int(stevilo)
except:
    print("Niste podali celega števila!")
    quit()

# preverjali bomo absolutno vrednost podanega števila
stevilo = abs(stevilo)

# izpišemo prvo vrstico izpisa
print(f"Delitelji števila {stevilo} so:")

# gremo po deliteljih od 1 dalje
trenutno_stevilo = 1
while trenutno_stevilo <= stevilo:
    #izračunamo ostanek pri deljenju števila s trenutnim številom
    ostanek = stevilo % trenutno_stevilo
    # preverimo, kakšen je ostanek deljenja izbranega števila z i
    if ostanek == 0:
        print(trenutno_stevilo)
    trenutno_stevilo = trenutno_stevilo + 1