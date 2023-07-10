from fractions import Fraction

# Task_1 Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
# num = int(input("Ведите число: "))
# sys_s = int(input("Введите систему счисления: "))
# res = " "
#
# print(f'Проверка через ф-ию hex: {hex(num)[2:].upper()}')
#
# while num > 0:
#     res = str(num % sys_s) + res
#     res_16 = res.replace("10", "A").replace("11", "B").replace("12", "C").replace("13", "D").replace(
#         "14", "D").replace("15", "F")
#     num = num // sys_s
# print(f'Вычисление по формулам: {res_16}')


# print(hex(int(input()))[2:].upper())


# Task_2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
str_num = input("Введите выражение вида a/b+c/d:")

if "+" in str_num:
    num = str_num.split("+")
    num_1 = list(map(int, str(num[0]).split("/")))
    num_2 = list(map(int, str(num[1]).split("/")))
    res = str((num_1[0] * num_2[1] + num_2[0] * num_1[1])) + "/" + str(num_1[1] * num_2[1])
else:
    num = str_num.split("*")
    num_1 = list(map(int, str(num[0]).split("/")))
    num_2 = list(map(int, str(num[1]).split("/")))
    res = str((num_1[0] * num_2[0])) + "/" + str((num_1[1] * num_2[1]))
print(res)

