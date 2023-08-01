#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Program za računanje ploščine in obsega kroga. """

# vključimo modul math
import math

# določimo polmer
r = input("Vnesi polmer kroga: ")

# poskusimo pretvoriti r v številko
try:
    r = float(r)
except:
    print(f"'{r}' ni številka!")
    quit()

# izračunamo ploščino kroga
ploscina = math.pi * math.pow(r,2)
ploscina = round(ploscina,2)

# izračunamo obseg kroga
obseg =  2 * math.pi * r
obseg = round(obseg,2)

# izpišemo ploščino in obseg kroga
print(f"Ploščina kroga s polmerom {r} je {ploscina}.")
print(f"Obseg kroga s polmerom {r} je {obseg}.")