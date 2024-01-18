#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("*"*21)
print("* Risanje smrečice *")
print("*"*21)

# uporabnika prosimo, naj vpiše število
stevilo = input('Vnesi višino smrečice: ')

try:
    stevilo = int(stevilo)
except:
    print("Niste vnesli celega števila!")
    quit()

if stevilo < 0:
    stevilo = -stevilo
    print(f"-{stevilo} sem za vas pretvoril v {stevilo}.")

# poravnano sredinsko
n = 1
while n <= stevilo:
    stevilo_zvezdic = 2 * n - 1
    najvecje_stevilo = 2 * stevilo - 1
    stevilo_praznih = (najvecje_stevilo - stevilo_zvezdic) / 2
    stevilo_praznih = int(stevilo_praznih)
    print(" "*stevilo_praznih,"*"*stevilo_zvezdic,sep="")
    n += 1 