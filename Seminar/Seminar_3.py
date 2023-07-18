# Task_3
# ✔Создайте вручную кортеж содержащий элементы разных типов.
# ✔Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.
# from pprint import pprint
#
# my_tuple = (True, "String", 2, False, 5.16, 4-3j, [1, 4, 5], (3, 4, 6), {2, 5, 5, 7, 6}, {4, 7, 6}, 43, 'second')
#
# result_dict = {}
#
# for i in my_tuple:
#     if type(i).__name__ not in result_dict:
#         result_dict[type(i).__name__] = []
#     result_dict[type(i).__name__].append(i)
#
# pprint(result_dict)

# 2 variant--------------------------------------------------------
# type_cort = (True, 5, None, 'bool', False, 3.14, 65)
#
# my_dict = {}
# for k in type_cort:
#     my_dict[k] = [i for i in type_cort if type(i) == type(k)]
# print(my_dict)


# task_4 ✔Создайте вручную список с повторяющимися элементами.
# ✔Удалите из него все элементы, которые встречаются дважды.

# my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
#
# i = 0
# while i < len(my_list):
#     if my_list.count(my_list[i]) == 2:
#         temp = my_list[i]
#         my_list.pop(i)
#         my_list.pop(my_list.index(temp))
#         i -= 2
#     i += 1
#
# print(my_list)
#2variant----------------------------------------------------------
# my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
#
# i = 0
# while i < len(my_list):
#     if my_list.count(my_list[i]) == 2:
#         temp = my_list[i]
#         my_list.pop(i)
#         my_list.pop(my_list.index(temp))
#         i -= 2
#     i += 1
#
# print(my_list)
#--------------------------------------------
# my_list = [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9]
#
# i = 0
# while i < len(my_list):
#     if my_list.count(my_list[i]) == 2:
#         temp = my_list[i]
#         my_list.remove(temp)
#         my_list.remove(temp)
#     else:
#         i += 1
#
# print(my_list)


# task_5 ✔Создайте вручную список с повторяющимися целыми числами.
# ✔Сформируйте список с порядковыми номерами нечётных элементов исходного списка. ✔Нумерация начинается с единицы.

# my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
# num = []
#
# for i in range(len(my_list)):
#     if my_list[i]%2!=0:
#         num.append(i+1)
#
# print(num)
#variant2---------------------------------------------------
# my_list = [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9]
#
# result = []
#
# for i in range(len(my_list)):
#     if  my_list[i] % 2:
#         result.append(i+1)
#
# print(*result)
#
# 3variant---------------------------------------------------------
# print(my_list:= [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9])
#
# print(*[i+1 for i in range(len(my_list)) if my_list[i] % 2])



# task_6 Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

# string = input("Введите строку через пробел").split()
# string.sort()
# maxx = max([len(i) for i in string])
#
# for n, s in enumerate(string, 1):
#     print(f"{n}. {' ' * (maxx-len(s) + 1)}{s}")

#2variant-------------------------------------------

# task_7 ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

# string = input("Введите строку ")
# string = [i for i in input()]
# dict1 = {}
# for i in string:
#     dict1[i] = dict1.get(i, 1) + 1
#
# print(dict1)
#2variant--------------------------------------------------------------------------------------marat
# from collections import Counter
#
# obj = input('Введите строку >>> ')
#
# result1 = {}
# result2 = {}
# result3 = Counter(obj)
# result4 = {}
#
# for i in obj:
#     result1[i] = result1.setdefault(i, 0) + 1
#
# for i in obj:
#     if i not in result2:
#         result2[i] = obj.count(i)
#
# for i in obj:
#     if i not in result4:
#         result4[i] = 0
#     result4[i] += 1
#
# print(result1, result2, result4, result3, sep = '\n')

