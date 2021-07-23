
new_list = []
i = 1
while True:
    new_list.append(
        (input('Введите номер товара: '),
         dict({'name': str(input('Введите название: ')),
               'price': float(input('Введите цену: ')),
               'amount': int(input('Введите количество: ')),
               'units': str(input('Введите единцы измерения: ')),
        }))
    )

    if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет' or 'ytn' or 'no':
        break

    i += 1

print(f'список товаров:{new_list}')

analytics = dict({})
for product in new_list:
    for key, value in product[-1].items():
        if key in analytics:
            if value not in analytics.get(key):
                analytics.get(key).append(value)
        else:
            analytics.update({key: [value]})


print(f'собрана аналитика: {analytics}')