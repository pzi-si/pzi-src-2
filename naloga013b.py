#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Seštevanje števk naravnega števila
"""

# uporabnika prosimo, naj vpiše številko
stevilo = input('Vnesi večmestno celo število: ')

try:
    stevilo = int(stevilo)
except:
    print("Niste vnesli celega števila!")
    quit()

def sestej(x):
    sestevek = 0
    x_string = str(x)
    for i in range(0,len(x_string)):
        sestevek += int(x_string[i])
    return sestevek

while stevilo > 9:
    stevilo = sestej(stevilo)
    print(stevilo)