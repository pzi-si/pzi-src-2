#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sestavi program, ki prebere naravno število in ga izpiše v obratnem vrstnem redu.  """

# Pozovemo uporabnika, naj poda število
stevilo = input("Podajte število, ki ga želite obrniti: ")

# preštejemo, koliko znakov ima niz
dolzina = len(stevilo)

n = 1
obrat = ""
while n <= dolzina:
    obrat += stevilo[dolzina-n]
    n+=1

# izpišemo obratno število
print(f"Obrat števila '{stevilo}' je '{obrat}'.")