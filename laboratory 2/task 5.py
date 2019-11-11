
import re

print("Лабораторна робота №2\nСалтиков А.В. КМ-94\nВаріант №19\n")

print("Завдання №2:\nЗнаїодження найбільшого цілого числа: \n")

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

N = do_input_int("Введіть значення N\n ")
if N <= 1:
    print("неможлива операція")
else:
    for K in range (N):
        if 3*K < N:
            ans = K
    print("Найбільше K =",ans)
