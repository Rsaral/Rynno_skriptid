# Import 
from datetime import datetime
name = 'rünno saral' # ' märk tähendab String ehk sõne
age = 25 # Täisarv (integer)
height = 1.79 # Ujukomaarv (float)

print(name, age, height) # Väljasta kolm väärtust
# Kasutaja rünno saral vanuses 35 aastat ja pikkusega 1.79 meetrit laua taga
print(f'Kasutaja {name.title()} vanuses {age} ja pikkusega {height} meetrit istub laua taga.')
print(' Kasutaja ' + name + ' vanuses ' + str(age) + ' ja pikkusega 1.79 meetrit ' )
      

# Arvutamine
birth_year = datetime.now().year - age # Jooksev aasta - vanus
print(birth_year)

name = name.title() # Korrasta nimi ja kasuta sama muutujat
print(name[1]) # Väljund: ü
print(name[1:5]) # Väljund: ünno 
print(name[6:]) # Väljund: Saral
print(name[:5]) # Väljund: rünno
print(name[::-1]) 

age = input('Sisesta vanus: ')
age = int(age)
if age < 1 or age > 122: 
    print('Vanus on vales vahemikus (Lubatud on 1-122)')
elif age < 18:
    print ('Alaealine')
elif age < 65:
    print('Tööealine')
elif age < 100:
    print('pensionär')
else:
    print('Pikaealine')

place = input('Sisesta elukoht: ')
print(f'Sisestati: {place}')

if len(place) > 1 and len(place) <= 7:
    print(f'Lühikese nimega koht {place.title()}')
elif len(place) > 7:
    print(f'Pika nimega koht {place.title()}')
else:
    print('Nimi liiga lühike.')


    # Väljasta muutujate andmetüübid
    print(type(name))
    print(type(age))
    print(type(height))
    print(type(place))
    