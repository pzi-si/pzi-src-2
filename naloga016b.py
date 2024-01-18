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

# poravnano desno
n = 1
while n <= stevilo:
    print(" "*(stevilo-n),"*"*n,sep="")
    n += 1 