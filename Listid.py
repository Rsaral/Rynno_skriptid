places = [] # Tühi list

places.append('Kehtna') #Lisa lõppu
places.append('Rapla') # Lisa lõppu
places[1:1] = ['Tallinn', 'Pärnu'] # Lisa Kehtna ja Rapla vahele mingi teine 
places.extend(['Viljandi', 'Tartu', 'Rapla']) #Lisab lõppu
places.insert(2, 'Are') # Lisab Tallina ja Pärnu vahele
print(places)

# Kustutamine
places.remove('Rapla') # Kusutab esimese leitud Rapla, teine jääb alles! Kuna käsk on konkreetselt eemalda "Rapla"
places.pop(6) # Viimase kustutamine (7 kokku!)
del places[2] # Are kustutamine
print(places)

# Ülesanne lisa Rapla lõppu ja peale Pärnut
places.append('Rapla') # Lõppu
places.insert(3, 'Rapla') # Peale Pärnut
print(places)

place = places[-1] # Muutuja saab väärtuseks listi viimase elemendi
index = places.index(place) # Mitmes element on Rapla (ainult üks!)
count = places.count(place) # Mitu Raplat on listis
print(index, count) # Väljund: 3 (näitab, et Pärnu on kolmanda kohal, kui lugeda siis esimene indeks on 0 ja algab 1, 2 jne
# 2 näitab, mitu Raplat on nimekirjas 
# Kas Rapla omn nimekirjas?


if place in places:
    print(f'{place} on nimekirjas.')

# Koopia nimekirjast 
list_copy = places.copy()
list_list = list(places)

print(places)
print(list_copy)
print(list_list)

list_copy.sort() # A->Z
list_list.sort(reverse=True) # Z->A

print() # Tühi rida
print(list_copy)
print(list_list)

new_sorted_list = sorted(places, reverse=False) # A->Z
print(new_sorted_list)

# Tühjenda listi sisu
new_sorted_list.clear()
list_copy.clear()
list_list.clear()

print(new_sorted_list)
print(list_copy)
print(list_list)
print(places)

# Ülesanne: Väljasta listi places viimane element ilma [-1] kasutamata

print(places[len(places)-1])
print(places)

# Väljasta konsooli elemendi Pärnu keskmine täht trükitähena
print(places[2][2].upper())
# Pikem versioon
city = places[2] # Element
char = city[2].upper() # Täht 
print(char)


          