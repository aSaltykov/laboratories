import re

print("Лабораторна робота №2\nСалтиков А.В. КМ-94\nВаріант №19\nЗнаходження суми\n")

def do_input_float(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}(\.[0-9]{1,})?$', value)):
            flag = False
            value = float(value)
        else:
            print('Помилка')
    return value
def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print('Помилка')
    return value


x = do_input_float("Введіть значення змінної: ")
n = do_input_int("Введіть кількість операцій: ")
summa = 0
for i in range(1, n):
        summa = summa + (x-i) / i**2
print("Сума =", round(summa ,4))