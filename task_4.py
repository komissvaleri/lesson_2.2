
def my_func(a, b):
    for i in range(b * -1):
        a *= a
    return 1 / a

a = float(input("Введите положительное число: "))
b = int(input("Введите отрицательную степень: "))
print(my_func(a, b))


