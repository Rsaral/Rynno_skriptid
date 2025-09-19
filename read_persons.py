"""
Luua etteantud kasutajatele kasutajanimi ja e-posti aadress
KASUTAJANIMI:
    eesnimi.perenimi
    eesnimes eemaldada tühik ja/või sidekriips Mari Liis/Mari-Liis
    eemalda rõhumärgid ja täpitähed (äõüöšž.. jne)
    kasutajanimi on läbivalt väikeste tähtedega 
E-POSTI AADRESS
    kasutajanimi@asutus.com
KELLELE TEHA
    Sündinud 1990-1999 k.a.
UUE FAILI SISU ON:
    Eesnimi;Perenimi;Isikukood;Kasutajanimi;E-post
    Eesnimi;Perekonnanimi;Sünniaeg;Sugu;Isikukood <--- ORIGINAAL KUJU ON SELLINE CSV-failis
"""
import csv
import unicodedata

src = 'Persons.csv' # Algallikas, kust infot loeme
dst = 'Persons_accounts.csv' # Uus fail
header = 'Eesnimi;Perenimi;Isikukood;Kasutajanimi;E-post' # Uue faili päis
domain = '@asutus.com'

def strip_accents(s):
    """
    Eemaldab rõhumärgid ja täpitähed

        https://stackoverflow.com/questions/517923/
    """ 
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


with open(src, 'r', encoding='utf-8') as f: # Lugemiseks, algne
    with open(dst, 'w', encoding='utf-8') as d: # Kirjutamiseks, uus. Kui fail on oleas, siis kirjutab üle, kui puudub, siis tekitab.
        contents = csv.reader(f, delimiter=';') # Faili sisu muutujasse
        d.write(header + '\n') # Uude faili päis reavahetusega
        next(contents) # Vii lugemisjärg järgmisele reale

        for row in contents:
            date = row[2] # Kuupäev eraldi muutujasse
            year = int(date.split('.')[2]) # Võta aasta kuupäevast ja tee int ehk täisarv
            
            if year >=1990 and year <=1999:
                first_name = row[0] # Eesnimi eraldi muutujasse
                last_name = row[1] # Perenimi eraldi muutujasse

                # Eemalda tühik ja sidekriips
                first_name = first_name.replace(' ','') # Tühik
                first_name = first_name.replace('-','') # Sidekriips

                #Kasutajanime loomine
                username = '.'.join([first_name, last_name]).lower()
                username = strip_accents(username)
                
                 # E-posti loomine
                email = username + domain
                
                # Uue rea loomine
                new_line = ';'.join(row[:2] + [row[-1], username, email])
                d.write(new_line + '\n')
                

                print(row[0], row[1], first_name, last_name, username, email)
 