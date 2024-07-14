def fekvo(szam): 
  
     if szam >= 0 or szam <= 100:
        return 'Negyzet'
    
     elif szam >= 101  or szam <= 299:
        return 'allo Teglalap'
     elif szam >= 300 or szam <= 999999999:
        return 'fekvo teglalap'    
     else:
        print('Helytelen adatokat adtal meg,csak szamok legyenek!')

while True:
     adat1 = input('Kerem adja meg a teglalap szelesseget:')
     adat2 = input('Kerem adja meg a teglalap magassagat:')
     if adat1 and adat2 == " " :
      break
      fekvo = int(fekvo)
     
     if adat1 and adat2 < 1:
        print('Kerem adjon meg 1-tol vegtelenig egy szamot')
     continue

      elif:

        print(f'Ez egy {fekvo}, Terulete {adat1 * adat2}')