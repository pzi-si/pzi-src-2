#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("-"*21)
print("| Fakulteta števila |")
print("-"*21)

# uvozimo modul math
import math

# uporabnika prosimo, naj vpiše število
stevilo = input('Vnesi število: ')

try:
    stevilo = int(stevilo)
except:
    print("Niste vnesli celega števila!")
    quit()

if stevilo < 0:
    print("Vnesli ste negativno število!")
    quit()

print(f"{stevilo}! = {math.factorial(stevilo)}")