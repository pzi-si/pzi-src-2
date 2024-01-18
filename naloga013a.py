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

while stevilo > 9:
    sestevek = 0
    stevilo_string = str(stevilo)
    for i in range(0,len(stevilo_string)):
        sestevek += int(stevilo_string[i])
    print(sestevek)
    stevilo = sestevek