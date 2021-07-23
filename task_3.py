
seasons = {'Winter': (1 ,2 ,12),
           'Spring': (2, 4 ,5),
           'Summer': (6, 7 ,8),
           'Autum': (9, 10, 11)}

month = int(input('Введите месяц от 1 до 12: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

