def honap(szam) :

    if szam == 1 or szam == 2 or szam ==12:

       return "Tel"

    elif szam >=3 and szam <=5 :

       return 'Tavasz'

    elif szam>= 6 and szam <= 8:

       return 'nyar'

    elif szam >= 9 and szam <= 11:

       return 'osz'
    else:

       return 'Nem letezo honap'



while True:

   jls_extract_var = int(input('Adja meg hanyadik honap van (1-12 kozott):'))
   Honap_szama = jls_extract_var
   if Honap_szama == '':

    print('Kilepes a programbol')

    break

   try:

    Honap_szama = int(Honap_szama)

    if Honap_szama < 1 or  Honap_szama > 12:

        print("Érvénytelen sorszám! Kérem, adjon meg egy sorszámot 1 és 12 között.")

        continue
    else:

        print(f'A {Honap_szama},honap az {honap(Honap_szama)} evszakhoz tartozik')

   except ValueError:

    print('Hibas bemenet! Kerem,csak szamot adjon meg.')