#1
from random import randint

print("Tere, maailm!")
nimi = input("Sisesta oma nimi : ")
print("Tere, maailm! Tervitan sind", nimi)
vanus = int(input("Sisesta oma vanus : "))
print("Tere, maailm! Tervitan sind", nimi, "!", "Sa oled", vanus, "aastat vana")

#2

'''
a) vanus = 18 tüüp int()
b) eesnimi = "Jaak" tüüp str()
c) pikkus = 16.5 tüüp float()
d) kas_käib_koolis = True tüüp Bool
print(type(...)) tüüpide kontrollimiseks
'''

#3
from random import randint
kommid = randint(1, 50)
print(kommid)
võetud = int(input("Mitu kommi soovid ära võtta"))
kommid -= võetud
print("Lauale jäi", kommid, "kommi")

#4
from math import pi
ümbermõõt = float(input("Siseta ümbermõõt : "))
läbimõõt = ümbermõõt / pi
print("Puu läbimõõt on", läbimõõt)

#5
from math import sqrt
N = float(input("Sisesta N :"))
M = float(input("Sisesta M :"))

diagonaal = sqrt(N**2 + M**2)
print("Diagonaali pikkus on :", diagonaal)

#6
'''
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus

print("Sinu kiirus oli " + str(kiirus) + " km/h")
õige foormula on teepikkus / aeg
'''

#7

a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input()),

summa = a + b + c + d + e

jagaja = int(input("Sisesta jagaja : "))

keskmine = summa / 5

print("Aritmeetiline keskmine:", keskmine)
print("Jagatise täisosa:", summa // jagaja)
print("Jagamise jääk:", summa % jagaja)

#8

print("@..@")
print("(----)")
print("( \__/ )")
print("^^ "" ^^ ")

#9
a, b, c = int(input()), int(input()), int(input())
perimetr = a + b + c

#10
hind = 12.90

inimeste_arv = int(input("Mitu inimest on kokku? "))

tips = hind * 0.10
kogusumma = hind + tips

inimese_hind = kogusumma / inimeste_arv

print("Iga inimene peab maksma", round(inimese_hind, 2), "eurot")
