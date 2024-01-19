#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("**********************************")
print("*** Ali je besedilo palindrom? ***")
print("**********************************")

# pozovemo uporabnika, naj vpiše besedilo
besedilo = input("Vpiši potencialen palindrom: ")

# obrnemo besedilo
obrnjeno_besedilo = besedilo[::-1]

# primerjamo besedili
if besedilo == obrnjeno_besedilo:
    print(f"Besedilo '{besedilo}' JE palindrom!")
else:
    print(f"Besedilo '{besedilo}' NI palindrom!")