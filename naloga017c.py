#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sestavi program, ki prebere naravno število in ga izpiše v obratnem vrstnem redu.  """

## OPOMBA: deluje samo za cela števila

# Pozovemo uporabnika, naj poda število
stevilo = input("Podajte število, ki ga želite obrniti: ")

if stevilo.isdigit() == False:
    print("Niste vnesli naravnega števila!")
    quit()

# preštejemo, koliko znakov ima niz
dolzina = len(stevilo)

n = 1
obrat = ""
while n <= dolzina:
    obrat += stevilo[dolzina-n]
    n+=1

# izpišemo vsoto
print(f"Obrat števila '{stevilo}' je '{obrat}'.")