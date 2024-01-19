#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sestavi program, ki prebere naravno število in ga izpiše v obratnem vrstnem redu.  """

# Pozovemo uporabnika, naj poda število
stevilo = input("Podajte naravno število, ki ga želite obrniti: ")

if stevilo.isdigit() == False:
    print("Niste vnesli naravnega števila!")
    quit()

# obrnemo
obrat = stevilo[::-1]

# izpišemo vsoto
print(f"Obrat števila '{stevilo}' je '{obrat}'.")