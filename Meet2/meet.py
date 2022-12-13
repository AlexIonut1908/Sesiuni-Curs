'''
if, else if, else
'''

optiune = int(input('alege optiune'))
if optiune == 0:
    print('meniu anterior')
elif optiune == 1:
    print('ati ales ro')
elif optiune == 2:
    print('ati ales eng')
else:
    print('mai incearca')
#
# EXERCITII
# 1
# Pentru un bancomat verificam userul si parola
# Userul si parola au doar doua incercari
# Userul doreste sa scoata o anumita suma de bani, acesta avand un sold curent
# Suma dorita trebuie sa fie mai mica sau egala decat soldul curent
# Daca introduci o suma prea mare poate sa aleaga daca doreste sa reincerce sau nu
# La a doua incercare, daca userul introduce din nou o suma prea mare, iese din program

# expected_user = 'Alex'
# expected_pass = '1234'
# sold = 500.49
# username = input('Introduceti username:')
# if username == expected_user:
#     print('User corect')
# else:
#     print('Username incorect. Incercati din nou')
#     username = input('Introduceti username:')
#     assert username == expected_user, 'Username incorect, o zi frumoasa!'
#     print('User corect')
#
# parola = input('Introduceti parola:')
# if parola == expected_pass:
#     print('Parola corecta!')
# else:
#     print('Parola incorecta! Incearca din nou')
#     parola = input('Introdu parola')
#     assert parola == expected_pass, 'Parola gresita! O zi frumoasa'
#     print('Parola corect')
#
# suma = float(input('Introdu suma dorita: '))
# if suma <= sold:
#     print('Ridicati banii')
# else:
#     print('Suma dorita este prea mare. Fonduri insuficiente')
#     reincercare = input('Doriti sa incercati din nou? Da/Nu: ')
#     if reincercare == 'Da':
#         suma = float(input('Introdu suma dorita: '))
#         assert suma <= sold, 'Suma introdusa este prea mare'
#         print('Ridicati banii')
#     elif reincercare == 'Nu':
#         print('La revedere')
#     else:
#         assert False, 'Eroare'


# 2
# joc de noroc cu zaruri
# avem un zar cu 6 fete
# primim de la tastatura un numar si sa verificam daca numarul este egal cu fata zarului care a fost aruncat

import random
zar = [1, 2, 3, 4, 5, 6]

diceRoll = random.choice(zar)

numar_Ales = int(input('Alege un numar: '))
if numar_Ales < diceRoll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_Ales}, dar a fost {diceRoll}')
elif numar_Ales > diceRoll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_Ales}, dar a fost {diceRoll}')
else:
    print('Ai ghicit, felicitari!')
