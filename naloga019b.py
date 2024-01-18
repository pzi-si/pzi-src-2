#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sestavi program, ki izračuna največji skupni delitelj števil a in b in izpiše vse vmesne rezultate evklidovega algoritma. """

import math

# Izpišemo, za kakšen program gre
print("*"*90)
print("*"*5,"Program za izračun največjega skupnega delitelja","*"*5)
print("*"*90)

# definirajmo funkcijo, ki nam bo preverila, če sta vnešeni številki celi
def preveriStevilke(stevilka):
    try:
        stevilka = int(stevilka)
        return stevilka
    except:
        print("'{}' ni številka.".format(stevilka))
        quit()

# Pozovemo uporabnika, naj poda dve celi številki
stevilo1 = input("Podajte prvo celo število: ")
# preverimo številki
stevilo1 = preveriStevilke(stevilo1)

stevilo2 = input("Podajte drugo celo število: ")
stevilo2 = preveriStevilke(stevilo2)

print("-"*90)

# preverimo, katero število je večje in določimo spremenljivki a in b
if (stevilo1 > stevilo2):
    a = stevilo1
    b = stevilo2
else:
    a = stevilo2
    b = stevilo1

# Evklidov algoritem
while b:
    n = math.floor(a/b)
    print("{} = {} * {} + {}".format(a,n,b,a%b))
    a,b=b,a%b
print("Največji delitelj števil {} in {} je {}.".format(stevilo1,stevilo2,a))