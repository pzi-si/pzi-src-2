#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sestavi program, s katerim ugibamo celo število med 1 in 100. """

## program pomaga najti rešitev

print("*********************************")
print("***** Igra: ugani številko! *****")
print("*********************************")

# vključim modul random, da bom lahko izbral naključen integer
import random

# izberem iskano številko
iskanaStevilka = random.randint(0,100)

steviloPoskusov = 0

stevilka = -1

while stevilka != iskanaStevilka:
    stevilka = input("Ugani številko med 0 in 100: ")
    steviloPoskusov += 1
    if stevilka.isnumeric(): 
        stevilka = int(stevilka)
        if stevilka != iskanaStevilka:
            if stevilka > iskanaStevilka:
                pomoc = "Iskana številka je manjša!"
            else:
                pomoc = "Iskana številka je večja!"
            print("Poskus št. {}. Nisi uganil. {} ni prava številka. {} Poskusi znova!".format(steviloPoskusov, stevilka, pomoc))
        elif stevilka == iskanaStevilka:
            print("Bravo! V {}. poskusu si uganil številko {}! Igra je končana!".format(steviloPoskusov, stevilka))
    else:
        print("Poskus št. {}. Vnesel si '{}', kar ni cela številka. Poskusi znova!".format(steviloPoskusov, stevilka))

