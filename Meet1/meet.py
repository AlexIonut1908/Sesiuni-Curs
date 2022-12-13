# simularea unui bancomat

'''
simularea unui bancomat
'''

expectedUserName = 'Alex'
expectedParola = '2424'
sold = 200
userName = input('User name: ')
assert expectedUserName == userName
parola = input('Parola este: ')
assert expectedParola == parola
plata = int(input('Suma de bani dorita: '))
assert plata >= plata