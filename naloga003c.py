#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Program za računanje ploščine in obsega kroga. """

# vključimo modul math
import math

# določimo polmer
r = 5

# izračunamo ploščino kroga
ploscina = math.pi * r**2

# izračunamo obseg kroga
obseg =  2 * math.pi * r

# izpišemo ploščino in obseg kroga
print(f"Ploščina kroga s polmerom {r} je {ploscina}.")
print(f"Obseg kroga s polmerom {r} je {obseg}.")