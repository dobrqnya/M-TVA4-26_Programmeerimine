
from math import sqrt, pi  # Kogu math-moodulit pole vaja importida.

# RUUT

print("Ruudu karakteristikud")

a = float(input("Sisesta ruudu külje pikkus => "))
# input() annab teksti, float() muudab selle arvuks.

S = a ** 2
print("Ruudu pindala", S)

P = 4 * a
print("Ruudu ümbermõõt", P)
# Parandasin jutumärgid.

di = a * sqrt(2)
# Kasutan sqrt(), et arvutada ruudu diagonaal.

print("Ruudu diagonaal", round(di, 2))

print()


# RISTKÜLIK

print("Ristküliku karakteristikud")

b = float(input("Sisesta ristküliku 1. külje pikkus => "))
c = float(input("Sisesta ristküliku 2. külje pikkus => "))

S = b * c
print("Ristküliku pindala", S)
# Parandasin puuduvad jutumärgid.

P = 2 * (b + c)
# Lisatud korrutusmärk.

print("Ristküliku ümbermõõt", P)

di = sqrt(b ** 2 + c ** 2)
# Kasutan Pythagorase teoreemi diagonaali leidmiseks.

print("Ristküliku diagonaal", round(di, 2))

print()


# RING

print("Ringi karakteristikud")

r = float(input("Sisesta ringi raadiuse pikkus => "))
# Parandasin jutumärgid ja lisasin float().

d = 2 * r
# Lisatud korrutusmärk.

print("Ringi läbimõõt", d)

S = pi * r ** 2
# pi on matemaatiline konstant, mitte funktsioon.

print("Ringi pindala", round(S, 2))

C = 2 * pi * r
# Parandasin korrutamise.

print("Ringjoone pikkus", round(C, 2))
