#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Sestavi program, ki izračuna največji skupni delitelj podanih števil. """

import math

# Izpišemo, za kakšen program gre
print("*"*90)
print("*"*5,"Program za izračun največjega skupnega delitelja","*"*5)
print("*"*90)

# definirajmo funkcijo, ki nam bo preverila, če sta vnešeni številki celi
def preveriStevilke(stevilka):
    try:
        stevilka = int(stevilka)
        return stevilka
    except:
        print("'{}' ni številka.".format(stevilka))
        quit()

# Pozovemo uporabnika, naj poda števila
stevila = input("Podajte števila, katerih največji skupni delitelj iščete (ločite jih z vejico): ")

# sestavimo seznam s števili
stevila_string = stevila.split(",")

stevila = []

# preverimo števila
for i in stevila_string:
    i = preveriStevilke(i)
    stevila.append(i)

print("Vnesli ste številke:",stevila)
print("-"*90)

i = 1
while i < len(stevila):
    if i == 1:
        j = i - 1
        a = stevila[i]
        b = stevila[j]
    else:
        a = stevila[i]
        b = delitelj
# preverimo, katero število je večje in določimo spremenljivki a in b
    if (a > b):
        a,b=b,a

    print("Preglejujem številki {} in {}.".format(a,b))
    # Evklidov algoritem
    while b:
        n = math.floor(a/b)
        print("{} = {} * {} + {}".format(a,n,b,a%b))
        a,b=b,a%b
    delitelj = a
    print("Največji skupni delitelj števil {} in {} je {}.".format(stevila[i],stevila[j],delitelj))
    print("-"*90)
    i += 1

print("Največji skupni delitelj števil {} je {}.".format(stevila_string,delitelj))