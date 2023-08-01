#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Izpišemo, za kakšen program gre
print("*"*54)
print("*"*5,"Program za pretvarjanje °C v °F in obratno","*"*5)
print("*"*54)

# navodilo
print("Podajte vrednost, ki jo želite pretvoriti.")
print("Dodajte C, če je vrednost v °C, in F, če je vrednost v °F. Primer: '23 C'")

# uporabnik poda vrednost 
vnos = input('Vnesite stopinje: ')

# odstranimo morebitne presledke na začetku in koncu vnosnega niza znakov
vnos = vnos.strip()

# preberemo zadnji znak
lestvica = vnos[-1]

# preberemo stopinje
temperatura = vnos[:-1]

# odstranimo morebitne presledke na začetku in koncu vnosnega niza znakov
temperatura = temperatura.strip()

# poskusimo spremeniti tip spremenljivke iz 'string' v 'float'
try:
    temperatura = float(temperatura)
except:
    print(f"Podana vrednost ni število. Podali ste {vnos}.")
    quit()

# preverimo, ali pretvarjamo °F v °C ali °C v °F
if lestvica == "C" or lestvica == "c":
    # pretvorimo F v C
    temperaturaF = (temperatura)*1.8+32

    # izpišemo rezultat pretvorbe
    print(f"{temperatura} °C = {temperaturaF} °F")
elif lestvica == "F" or lestvica == "f":
    # pretvorimo F v C
    temperaturaC = (temperatura - 32)*5/9

    # zaokrožimo C na 1 decimalko
    temperaturaC = round(temperaturaC,1)

    # izpišemo rezultat
    print(f"{temperatura} °F = {temperaturaC} °C")
else:
    # ne pretvarjamo ne F in ne C
    print("Niste določili, po kateri lestvici je vrednost, ki ste jo podali.")