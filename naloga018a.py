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

# obrnemo besedilo
obrnjeno_besedilo = besedilo[::-1]

i = 0
palindrom = True
while i < len(besedilo):
    if besedilo[i] != obrnjeno_besedilo[i]:
        palindrom = False
    i += 1

if palindrom:
    print("Besedilo '{}' JE palindrom!".format(besedilo))
else:
    print("Besedilo '{}' NI palindrom!".format(besedilo))