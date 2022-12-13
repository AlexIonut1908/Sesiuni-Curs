# dalmatienii
for i in range(1, 102):
    print(f'Dalmatianul cu numarul {i}')

# dalmatienii din 2 in 2
for i in range(1, 102, 2):
    print(f'Dalmatianul cu numarul {i}')

numere = [3, 7, 10, 20, 30]
# parcurgere lista cu for prin intermediul indexului
for i in range(0, len(numere)):
    print(f'indexul curent este {i}')
    print(f'numarul curent este {numere[i]}')

# for each
suma = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    suma = suma + numar
print(f'Suma este {suma}')

# de cate ori apare 3 in {3, 2, 3, 5, 3]

numere = [3, 2, 3, 5, 3]
suma = 0
for numar in numere:
    suma = suma + numar
print(f'Suma este de: {suma}')