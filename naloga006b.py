#!/usr/bin/env python
# -*- coding: utf-8 -*-

#T(°C) = (T(°F) - 32 °F)/1,8
#T(°F) = 1,8 T(°C) + 32

# Izpišemo, za kakšen program gre
print("*"*73)
print("*"*5,"Program za pretvarjanje stopinj Celzija v stopinje Fahrenheita","*"*5)
print("*"*73)

# Podajte 
temperaturaC = input('Vnesite °C: ')

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
try:
    temperaturaC = float(temperaturaC)
except:
    print(f"Podana vrednost ni število. Podali ste {temperaturaC}.")
    quit()

# pretvorimo F v C
temperaturaF = (temperaturaC)*1.8+32

# zaokrožimo C na 1 decimalko
temperaturaF = round(temperaturaF,1)

# izpišemo rezultat
print(f"{temperaturaC} °C = {temperaturaF} °F")