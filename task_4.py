
text = input('Введите строку из нескольких слов: ')
a = text.split(' ')
for i, a in enumerate(a):
    print(f'{i+1}  {a[:10]}')


