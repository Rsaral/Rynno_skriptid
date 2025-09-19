import random

names = ['Mari', 'Anna', 'Villem', 'Jüri']

# Väljasta listis olevad nimed nime kaupa eraldi real.
for name in names: 
    print(name) 
print()

# Teistmoodi väljastus
for x in range(len(names)): # x = 0...3
    print(names[x], random.randint(1, 122))
print()

# Lihtsalt numbrid
for x in range (1, 5): # 1, 2, 3, 4, 5
    print(x, end=' ')
print('\n') # Kaks reavahetust!

for x in range(0, 10, 2): #Paarisarvud
    print(x, end=' | ')
print('\n')

x = 0 
while x < len(names):
    print(names[x])
    x += 1 # X=x+1
print(x)

""" 
Ülesanne: väljasta listi nimed konsooli iga nimi eraldi real, kuid iga nime ees on järjekorra number. Järjekorra number algab ühega.
Korrektne rida on järgnev:
1. Mari
2. Anna
3. Villem
4. Jüri


Täiendus: tee igale nimele juhuslik vanus, kuid kirjuta see vanus listi nimega ages. Näita tulemust samas for või while loopis. 
Peale kordust näita nii names, kui ages listi sisu lihtsalt nagu listid.py failisi näitasime
"""

names = ["Mari", "Anna", "Villem", "Jüri"]
ages = []
for i, name in enumerate(names, start=1):
    
    ages.append(random.randint(1, 110))
    print(f"{i}. {name} {ages[i-1]}")

print(ages)
print(names)

    
