# def contBancar(userName, parola, plata):
#     i = 0
#     while i < 3:
#         if userName == 'Alex Ionut':
#             if parola == '2424':
#                 if plata <= 200:
#                     print('Tranzactie reusita')
#                     break
#                 else:
#                     print('Fonduri insuficiente')
#                     break
#             else:
#                 print('Parola incorecta')
#                 parola = input('Parola: ')
#                 i += 1
#         else:
#             print('Username gresit')
#             userName = input('ID: ')
#             i += 1
#     print('Multumuim. O zi frumoasa')
#
# contBancar(input('ID: '), input('Parola: '), int(input('Sold: ')))

def bubblesort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

listSortata = bubblesort([3, 6, 8, 1, 4, 9, 0, 10])
print(listSortata)

# def listMax(list):
#     listSortata = bubblesort(list)
#     return listSortata[-1]
# maxim = listMax([3, 6, 8, 1, 4, 9, 0, 10])
# print(maxim)
#
# def listMax2(list):
#     maxim = 0
#     for i in range(len(list):
#         if maxim ( list[i]):
#     maxim = list[i]



# import random
#
# def diceRoll():
#     zar = [1, 2, 3, 4, 5, 6]
#     numarZar = random.choice(zar)
#     numarAles = int(input('Alege un numar: '))
#     if numarAles < numarZar:
#         print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numarAles}, dar a fost {numarZar}')
#     elif numarAles > numarZar:
#         print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numarAles}, dar a fost {numarZar}')
#     else:
#         print('Ai ghicit, felicitari!')
#
# diceRoll()
# diceRoll()
# diceRoll()
# diceRoll()
# diceRoll()
# diceRoll()
# diceRoll()