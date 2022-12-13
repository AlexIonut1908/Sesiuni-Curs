lista = [3, 6, 8, 1, 4, 9, 0, 10]
for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if lista [j] > lista[j+1]:
            lista [j], lista[j+1] = lista[j+1], lista[j]

print(lista)