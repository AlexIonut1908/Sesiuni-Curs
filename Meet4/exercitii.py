list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for var in list1:
    sum = var + sum
print(sum)

list1 = [7, 8, 10, 4, 5, 6, 7, 8, 9, 10]
i = 0
sum = 0
while i < len(list1):
    sum = sum + list1[i]
    i += 1
print(sum)

list2 = ['primavara', 'vara', 'toamna', 'iarna']
for anotimp in list2:
    if anotimp == 'toamna':
        break
    print(anotimp)

for anotimp in list2:
    if anotimp == 'vara':
        continue
    print(anotimp)

# bubble sort, intersection sort, merch sort, quick sort

# bubble sort
list = [3, 6, 8, 1, 4, 9, 0, 10]
for i in range(len(list)-1):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
         list[j], list[j+1] = list[j+1], list[j]
print(list)