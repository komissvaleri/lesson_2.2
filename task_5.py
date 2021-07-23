
number = int(input('Элемент рейтинга: '))

list_a = [7, 5, 3, 3, 2]
b = list_a.count(number)
inserted = False
for ind, el in enumerate(list_a):
    if number > el:
        list_a.insert(ind, number)
        inserted = True
        break

if not inserted:
    list_a.append(number)

print(list_a)