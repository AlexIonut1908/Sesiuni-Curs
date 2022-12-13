def printGreeting():
    print('Buna ziua! Bine ati venit')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def piValue():
    return (3.14)

# exercitiu: daca numarul este pozitiv, returneaza true, altfel false
# daca persoana este majora
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

# zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('A', 'Asd')
printGreetingByName('S', 'Andy')
printGreetingByName('C', 'Bro')
print(mediaNr(3,3,4))
print(piValue())
print(verificareMajor(18))

# se ia varsta utilizatorului
age = int(input('Introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat. Bine ai venit in aplicatie!')
else:
    print('Nu ai varsta minima necesara (18) pentru a paria')

# oop
# variabile => atribute, proprietati sau fields
# functii => metode