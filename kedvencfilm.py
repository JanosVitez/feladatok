def percet_orava_es_perce(percek):
    orak = percek // 60
    maradek_percek = percek % 60
    return orak, maradek_percek

def main():
    film_cime = input("Kérem, adja meg a film címét: ")
    idotartam_perc = int(input("Kérem, adja meg a film időtartamát percekben: "))

    orak, maradek_percek = percet_orava_es_perce(idotartam_perc)
    
    print(f"A(z) '{film_cime}' című film {orak} óra és {maradek_percek} perc hosszú.")