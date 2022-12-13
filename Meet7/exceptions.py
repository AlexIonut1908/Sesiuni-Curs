try:
    lista = [1, 2, 3]
    lista[6]

except IndexError as e:    # except BaseException as e (cand vrem sa parcurga o singura exceptie)
    print(e)
print('Am ajuns aici')

raise IndexError('Eroare fortata')