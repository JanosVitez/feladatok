import random

#1.feladat
szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]

#2. feladat
rejtettszo = random.choice(szavak)
első_betű = rejtettszo[0]
print(f'Rejtett szó: {első_betű}.....')

#3. feladat
tipp = input("Kérem a tippet: ")
tipp_db = 1
stop = False
while tipp != rejtettszo:
    if tipp == "stop":
        stop == True
        break
    print("Az eredmény: ", end="")
    for i in range (min(len(tipp), len(rejtettszo))):
        if tipp[i] == rejtettszo[i]:
            print(tipp[i], end="")
        else:
            print(".", end="")
    print()
    tipp = input("\nKérem a tippet: ")
    tipp_db += 1

#4.feladat
if tipp == stop:
    print("sikeresen kiléptél")
else:
    print("gratulálok!")