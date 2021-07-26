
def int_func(text):
    slovo = text[0].upper() + text[1:].lower()
    return slovo

print(int_func(input('Введите слово с маленькой буквы: ')))



sentence = input('Введите предложение: ')
for slovo in sentence.split(' '):
    print(f'{int_func(slovo)}', end=' ')



