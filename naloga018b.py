#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Uporabnik vpiše niz znakov, program pa pove, ali je vpisan niz palindrom ali ne.
Palindrom je niz znakov, ki se enako prebere z leve in z desne.
"""

## tole deluje: pericarezeracirep
## tole ne deluje: perica reze raci rep

print("*********************************")
print("*** Ali je besedilo palindrom ***")
print("*********************************")


# pozovemo uporabnika, naj vpiše besedilo
besedilo = input("Vpiši potencialen palindrom: ")

# odstranimo presledke in vse velike črke spremenimo v male
cisto_besedilo = besedilo.replace(" ","").lower()
cisto_besedilo = cisto_besedilo.replace(".","").replace(",","").replace("!","")

# obrnemo besedilo
obrnjeno_besedilo = cisto_besedilo[::-1]

# primerjamo besedili
if cisto_besedilo == obrnjeno_besedilo:
    print(f"Besedilo '{besedilo}' JE palindrom!")
else:
    print(f"Besedilo '{besedilo}' NI palindrom!")