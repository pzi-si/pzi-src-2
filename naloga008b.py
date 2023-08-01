#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Napiši program, ki izpiše vse delitelje podanega števila. """

# Uporabnika pozovemo, da vpiše število, katerega delitelje bomo iskali
stevilo = input("Vpišite število, za katerega želite poiskati vse delitelje: ")

# preverimo, ali je podano število tipa 'integer'
try:
    stevilo = int(stevilo)
except:
    print("Niste podali celega števila!")
    quit()

# gremo po deliteljih od 1 dalje
trenutno_stevilo = 1

# uvedemo spremenljivko, kamor bomo zapisovali rezultate
delitelji = ""

while trenutno_stevilo <= stevilo:
    #izračunamo ostanek pri deljenju števila s trenutnim številom
    ostanek = stevilo % trenutno_stevilo
    # preverimo, kakšen je ostanek deljenja izbranega števila z i
    if ostanek == 0:
        delitelji = delitelji + str(trenutno_stevilo)
        # vejico izpišemo samo, če ne dodajamo zadnjega števila v nizu
        if trenutno_stevilo != stevilo:
            delitelji +=", "
    trenutno_stevilo = trenutno_stevilo + 1

#izpišemo delitelje
# začnemo izpis rezultatov
print(f"Delitelji števila {stevilo} so: {delitelji}")