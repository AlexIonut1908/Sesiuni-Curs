# liste
list1 = ['abc', 34, True, 40, 'male', 'male']
print(type(list1))
print(list1)
print(list1[0])
print(len(list1))

# dict
thisdict = {
    'brand': 'Volvo',
    'model': 'XC 60',
    'year': 2011
}
print(type(thisdict))
print(thisdict)
print(thisdict['brand'])
print(len(thisdict))

# set
thisset = {'alb', 'rosu', 'galben', 3, 7, 9}
print(type(thisset))
print(thisset)
print(len(thisset))

# tupla
tupla1 = (1, 2, 3, 4, (2, (3, 10, 20, 30), 4, 5))
print(type(tupla1))
print(tupla1)
print(tupla1[0])
print(tupla1[4])
print(tupla1[4][1][2])
print(len(tupla1))