"""
Sestavi program, ki bo za vpisano letnico preveril, ali je leto prestopno ali ne.

Pravilo za določanje prestopnih let je:

    Leto je prestopno, če je deljivo s 4, razen ...
    ... v primeru, da je leto deljivo s 100, leto ni prestopno, razen ...
    ... v primeru, da je leto deljivo s 400, leto je prestopno.
"""

print("******************************")
print("*** Ali je leto prestopno? ***")
print("******************************")


# pozovemo uporabnika, naj vpiše letnico
letnica = input("Vpiši letnico: ")

# preverimo, če je vpisana res letnica
try:
    letnica = int(letnica)
    if letnica > 9999 or letnica < -9999:
        print("Niste vnesli letnice!")
        quit()
except:
    print("Niste vnesli letnice!")
    quit()

# uvedemo spremeljivko prestopno
prestopno = False

if letnica % 400 == 0:
    prestopno = True
elif letnica % 4 == 0 and letnica % 100 == 0:
    prestopno = False
elif letnica % 4 == 0:
    prestopno = True

if prestopno:
    print("Leto {} JE prestopno!".format(letnica))
else:
    print("Leto {} NI prestopno!".format(letnica))
    