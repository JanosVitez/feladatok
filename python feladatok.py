#1. feladat.
''''
num1 = float(input("Kérem adja meg az első számot: "))
num2 = float(input("Kérem adja meg a második számot: "))
num3 = float(input("Kérem adja meg a harmadik számot: "))

min_num = min(num1, num2, num3)

print("A három szám közül a legkisebb:", min_num)
''''

#2.feladat.

''''
num1 = float(input("Kérem adja meg az első számot: "))
num2 = float(input("Kérem adja meg a második számot: "))
num3 = float(input("Kérem adja meg a harmadik számot: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    print("A három szám különböző.")
else:
    print("A három szám nem különböző.")
''''

#3.feladat.

''''
pontszam = int(input("Kérem adja meg a dolgozat pontszámát: "))

if pontszam < 50:
    print("Érdemjegy: 1")
elif pontszam < 60:
    print("Érdemjegy: 2")
elif pontszam < 70:
    print("Érdemjegy: 3")
elif pontszam < 85:
    print("Érdemjegy: 4")
else:
    print("Érdemjegy: 5")
''''

#4.feladat

szam = int(input("Kérem adjon meg egy egész számot: "))

if szam % 3 == 0 or szam % 5 == 0:
    print("Igen, a szám osztható 3-mal vagy 5-tel.")
else:
    print("Nem, a szám nem osztható sem 3-mal, sem 5-tel.")
