filename = 'Persons.csv'
total = 0

phrase = input('Sisesta otsitav fraas (min. 2 märki): ')

if len(phrase.strip()) > 1:
    phrase = phrase.strip().lower() # Korrasta otsingu fraas
    f = open(filename, 'r', encoding='utf-8') # Ava fail lugemiseks
    contents = f.readlines()[1:] # Alates teisest reast
    f.close() # Sulge fail
    for line in contents: # Käi list rea kaupa läbi
        line = line.strip() # Korrasta rida (eemalda reavahetus reast \n)
        if phrase in line.lower(): # Kas fraas on reas olemas 
            print(line) # Väljasta rida 
            total += 1 # Suurenda loendurit

    print(f'Leiti {total} nime.') # Leitud ridade/nimede arv    

else:
    print('Otsinug fraas on liiga lühike!')