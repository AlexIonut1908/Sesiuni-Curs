'''
Operatori:
aritmetici: +, -, *, /, % , **
de comparare: < >, ==, !=, >=, <=
logici:and , or, !
'''

a = 3
b = 5

print(a + b) # 3+5 => 8
print(a == b) # a este egal cu b?  => False
print(a < b and a < 4) # True SI True  => True
print(a < b or a < 2) # True SAU False  => True

# cu mama sau tata sau (cu bunicu si bunica)
mama = True
tata = False
bunicu = False
bunica = False
print(mama or tata or (bunicu and bunica)) # True

mama = False
tata = False
bunicu = True
bunica = False
print(mama or tata or (bunicu and bunica)) # False

mama = False
tata = False
bunicu = True
bunica = True
print(mama or tata or (bunicu and bunica)) # True

mama = True
tata = True
bunicu = True
bunica = True
print(mama or tata or (bunicu and bunica)) # True