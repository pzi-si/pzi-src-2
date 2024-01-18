#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("-"*21)
print("| Fakulteta števila |")
print("-"*21)

# uporabnika prosimo, naj vpiše število
stevilo = input('Vnesi število: ')

try:
    stevilo = int(stevilo)
except:
    print("Niste vnesli celega števila!")
    quit()

if stevilo < 0:
    print("Ne morem izračunati fakultete negativnega števila!")
    quit()

if stevilo == 0 or stevilo == 1:
    print(f"{stevilo}! = 1")
else:
    izpis = []
    n = stevilo
    fakulteta = 1
    while n > 0:
        izpis.append(str(n))
        fakulteta *= n
        n -= 1

    izpis = ' * '.join(izpis)
    print(f"{stevilo}! = {izpis} = {fakulteta}")