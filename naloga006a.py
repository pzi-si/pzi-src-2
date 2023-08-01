#!/usr/bin/env python
# -*- coding: utf-8 -*-

#T(°C) = (T(°F) - 32 °F)/1,8
#T(°F) = 1,8 T(°C) + 32

# Izpišemo, za kakšen program gre
print("*"*73)
print("*"*5,"Program za pretvarjanje stopinj Fahrenheita v stopinje Celzija","*"*5)
print("*"*73)

# Podajte 
temperaturaF = input('Vnesite °F: ')

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
try:
    temperaturaF = float(temperaturaF)
except:
    print(f"Podana vrednost ni število. Podali ste {temperaturaF}.")
    quit()

# pretvorimo F v C
temperaturaC = (temperaturaF - 32)*5/9

# zaokrožimo temperaturo v °C na 1 decimalko
temperaturaC = round(temperaturaC,1)

# izpišemo rezultat
print(f"{temperaturaF} °F = {temperaturaC} °C")