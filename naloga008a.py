#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Napiši program, ki izpiše vse delitelje podanega števila.
Sestavi program, ki dobi število n in izpiše vse njegove delitelje, vsakega samo enkrat, urejene po velikosti.
 """

# Uporabnika pozovemo, da vpiše število, katerega delitelje bomo iskali
stevilo = input("Vpišite število, za katerega želite poiskati vse delitelje: ")

# preverimo, ali je podano število tipa 'integer'
try:
    stevilo = int(stevilo)
except:
    print("Niste podali celega števila!")
    quit()

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