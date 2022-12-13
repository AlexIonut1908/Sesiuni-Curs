# 1. Liste
lista_goala = []
# listele in python pot sa cuprinda elemente de tipuri diferite
# au dimensiune dinamica
# sunt structuri de date ordonate
fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in functie de index
print(fructe[1])

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'

# afisam lista
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print('ultimul element: ', last)
print('lista: ', fructe)

# de cate ori apare un element
print(fructe.count(3))

# extindem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)

# 2.dict
dict_gol = []
# declaram si initializam un dict
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

# adaugam elemente
note_elevi['Sebi'] = 7

# printam dict-ul
print(note_elevi)

# aflam elemente
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# stergem valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu mai avem acest elev'))
print(note_elevi.pop('Gigel', 'nu mai avem acest elev'))
print(note_elevi)

# returneaza doar cheila
print(note_elevi.keys())