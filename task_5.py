
def str_numb(numbers, stop_sim):
    parts = numbers.split(' ')
    sum_1 = 0
    for i in parts:
        if i == stop_sim:
            break
        sum_1 += int(i)

    return sum_1

stop_sim = '*'
finished = False
s = 0
while not finished:
        numbers = input("Введите числа через пробел: ")
        s += str_numb(numbers, stop_sim)
        finished = stop_sim in numbers
        print(f'Sum = {s}')

