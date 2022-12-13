piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par printam acest lucru
# altfel printam impar
nr = 1
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? impartirea ne da restul 0 (% - modulo)
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

if nr % 5 == 0:
    print('nr par')
else:
    print('impar')

# este un nr pozitiv?
if (nr > 0):
    print('pozitiv')
else:
    print('nr nu este pozitiv')

#daca utilizatorul are sub 18 ani, nu poate paria. TEMA

# DACA LA LINIA 12 PUNEM 0, REZULTATUL VA FI "NU ESTE POZITIV"!!!

# if, else if, else
# cum ne saluta robotelul in functie de ora?

# luam date de la tastatura
# ne asiguram ca sunt transformate din string in int
# ora = int(input('Introdu ora'))
##print(ora == 17)

# if ora < 0:
#     print('ora negativa')
# elif ora <= 11:
#     print('Buna dimineata!')
# elif ora <= 18:
#     print('Buna ziua!')
# elif ora <= 21:
#     print('Buna seara!')
# elif ora <= 24:
#     print('Noapte buna!')
# else:
#     print('ora invalida, ora mai mare decat 24')
#CTRL + /

# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales romana')
elif optiunea == 2:
    print('ati ales engleza')
else:
    print('nu am identificat optiunea, mai incearca')
