#                WHILE

i = 0
while i <= 10:
    print(i)
    i += 1
print('Done')

#                FOR ELSE

for i in range(10):
    print(i)

for i in range(4, 10):
    print(i)

for i in range(20, 10, -1):
    print(i)
else:
    print('Done')

#                FOR EACH

culori = ['rosu', 'albastru', 'negru', 'alb']   # lista este clasa
for culoare in culori:
    print(culoare)

for i in range(len(culori)):
    print(culori[i])

#                BREAK
i = 0
while(i <= 100000):
    print(i)
    if i == 5:
        break
    i += 1

i = 0
while i <= 1:
    print(f'Valoare lui i este {i}')
    i += 1
    if i >= 40:
        break
print('Ceva')

#                CONTINUE

culori = ['rosu', 'albastru', 'negru', 'alb']

for culoare in culori:
    if culoare == 'negru':
        continue
    print(culoare)