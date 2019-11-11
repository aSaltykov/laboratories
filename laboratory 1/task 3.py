import math
import re

print("Салтиков А.В \nЛабораторна робота №1 \nВаріант 19 \nОбчислення функції в залежності від значень x.  \n")

def do_float(text):
    flag = False
    while not flag:
        value = input(text)
        if bool(re.match('^[+-]{0,1}[0-9]{1,}(\.[0-9]{1,}){0,1}$', value)):
            flag = True
            value = float(value)
        else:
            print("Сталася помилка. Спробуйте ще раз")
    return value


x = do_float("Введіть x: ")

if x>-4:
    x = math.cos(2*x)+9
    print(x)
else:
    x = ((math.cos(x))/x-9)*-1
    print("Значення функції",x)