class Beteg:
    def __init__(self, nev="", TAJ="", sorszam=0):
        self.nev = nev
        self.TAJ = TAJ
        self.sorszam = sorszam

    def varakozas(self):
        return self.sorszam * 5

betegek = []

for i in range(3):
    nev = input("Add meg a beteg nevét! ")
    TAJ = input("Add meg a beteg TAJ számát! ")
    beteg = Beteg(nev, TAJ, i)
    betegek.append(beteg)

for beteg in betegek:
    print(f"{beteg.sorszam}. {beteg.nev} {beteg.TAJ}, Várható várakozás: {beteg.varakozas()} perc.")
