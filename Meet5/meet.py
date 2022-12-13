def print_hi():
    print('Hello Worlds')
    print('Hello 2')
    print('Hello 3')

print_hi()
print_hi()
print_hi()

def print_hi(user, age=None):
    print(f'Hi {user}!')
    print(age)

print_hi('Andy')
print_hi('Andrei')
print_hi('Andrei', 44)

def is_natural(numar):
    if numar >= 0:
        return True
    else:
        return False

raspuns = is_natural(4)
if raspuns :
    print('Numarul este natural')
else:
    print('Numarul nu este natural')

raspuns = is_natural(-4)
if raspuns :
    print('Numarul este natural')
else:
    print('Numarul nu este natural')

if (is_natural(4)):
    print('Numarul este natural')
else:
    print('Numarul nu este natural')

if (is_natural(-4)):
    print('Numarul este natural')
else:
    print('Numarul nu este natural')
