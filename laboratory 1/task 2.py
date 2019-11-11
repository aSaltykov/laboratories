import math
import re

print("Салтиков А.В \nЛабораторна робота №1 \nВаріант 19 \nРозпізнання прямокутних трикутників.  \n")

def do_float(text):
    flag = False
    while not flag:
        value = input(text)
        if bool(re.match('^[+]{0,1}[0-9]{1,}(\.[0-9]{1,}){0,1}$', value)):
            flag = True
            value = float(value)
        else:
            print("Сталася помилка. Спробуйте ще раз")
    return value

a = do_float("Введіть сторону a: ")
b = do_float("Введіть сторону b: ")
c = do_float("Введіть сторону c: ")

if a**2 + b**2 == c**2:
    print("Трикутник прямокутний")

elif a**2 + c**2 == b**2:
    print("Трикутник прямокутний")


elif c**2 + b**2 == a**2:
    print("Трикутник прямокутний")

else:
    сosc = (a * a + b * b - c * c) / (2 * a * b)

print(math.acos(сosc) * 57.2958)