
list_a = ['a', 'b', 'c', 'd', 'e']
if len(list_a) % 2 ==0:
    i = 0
    while i < len(list_a):
        el = list_a[i]
        list_a[i] = list_a[i+1]
        list_a[i+1] = el
        i += 2
else:
    i = 0
    while i < len(list_a) - 1:
        el = list_a[i]
        list_a[i] = list_a[i+1]
        list_a[i+1] = el
        i +=2
print(list_a)


