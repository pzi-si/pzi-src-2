#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("******************************")
print("*** Ali je leto prestopno? ***")
print("******************************")

# pozovemo uporabnika, naj vpiše letnico
letnica = input("Vpiši letnico: ")

# preverimo, če je vpisana res letnica
try:
    letnica = int(letnica)
    # omejimo letnice na obseg od -9999 do 9999
    if letnica > 9999 or letnica < -9999:
        print("Niste vnesli letnice!")
        quit()
except:
    print("Niste vnesli letnice!")
    quit()

# uvedemo spremeljivko prestopno
prestopno = False

# če je letnica deljiva s 400, je leto prestopno
if letnica % 400 == 0:
    prestopno = True
# če ni deljiva s 400, je pa deljiva s 4 in 100, potem leto ni prestopno
elif letnica % 4 == 0 and letnica % 100 == 0:
    prestopno = False
# letnica je deljiva s 4, ni pa hkrati deljiva s 100 -> leto je prestopno
elif letnica % 4 == 0:
    prestopno = True

if prestopno:
    print(f"Leto {letnica} JE prestopno!")
else:
    print(f"Leto {letnica} NI prestopno!")