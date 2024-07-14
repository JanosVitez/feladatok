#1.feladat

''''
szamok = []
while len(szamok) < 5:
    szam = int(input(f"Kérem adjon meg egy {len(szamok) + 1}. számot (1 és 99 között): "))
    if 1 <= szam <= 99:
        szamok.append(szam)
    else:
        print("Hibás bemenet! A számnak 1 és 99 között kell lennie.")

print("Bekért számok:", szamok)

paros_szamok = [szam for szam in szamok if szam % 2 == 0]
if paros_szamok:
    print("Páros számok:", paros_szamok)
else:
    print("Nincs páros szám a bekért számok között.")
''''

#2.feladat

''''
szam1 = float(input("Kérem adja meg az első számot: "))
szam2 = float(input("Kérem adja meg a második számot: "))
szam3 = float(input("Kérem adja meg a harmadik számot: "))


if szam1 + szam2 == szam3 or szam1 + szam3 == szam2 or szam2 + szam3 == szam1:
    print("Igen, a számok közül legalább két szám összege egyenlő a harmadik számmal.")
else:
    print("Nem, a számok közül egyik pár összege sem egyenlő a harmadik számmal.")
''''

#3.feladat.

''''
szam1 = float(input("Kérem adja meg az első számot: "))
szam2 = float(input("Kérem adja meg a második számot: "))

szam1, szam2 = szam2, szam1

print("Az értékek felcserélve:")
print("Első szám:", szam1)
print("Második szám:", szam2)
''''

#4.feladt

while True:
    try:
        start = int(input("Kérem adja meg az intervallum kezdő számát (pozitív egész szám): "))
        end = int(input("Kérem adja meg az intervallum végpontját (pozitív egész szám): "))
        if start <= 0 or end <= 0:
            raise ValueError("A megadott számoknak pozitívnak kell lenniük.")
        break
    except ValueError as ve:
        print(ve)

print("A páros számok az intervallumban:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)

