#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("-"*21)
print("| Fakulteta števila |")
print("-"*21)

# uporabnika prosimo, naj vpiše število
stevilo = input('Vnesi število: ')

def fakulteta(stevilo):
    try:
        stevilo = int(stevilo)
        if stevilo < 0:
            rezultat = "Ne morem izračunati fakultete negativnega števila!"
        elif stevilo == 0 or stevilo == 1:
            rezultat = f"{stevilo}! = 1"
        else:
            izpis = []
            n = stevilo
            fakulteta = 1
            while n > 0:
                izpis.append(str(n))
                fakulteta *= n
                n -= 1

            izpis = ' * '.join(izpis)
            rezultat = f"{stevilo}! = {izpis} = {fakulteta}"
    except:
        rezultat = "Niste vnesli celega števila!"
    return rezultat

print(fakulteta(stevilo))