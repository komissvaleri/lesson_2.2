
def my_func(a, b, c):
    d = [a, b, c]
    d.remove(min(a, b, c))
    return sum(d)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
sum_1 = my_func(a, b, c)
print(sum_1)





