
def fun_1(num_1, num_2):
    if num_2 == 0:
        return 'На ноль делить нельзя'
    else:
        return num_1 / num_2

num_1 = int(input("Введите делимое: "))
num_2 = int(input("Введите делитель: "))
print(fun_1(num_1, num_2))

