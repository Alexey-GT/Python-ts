import os


# ✔Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.


# def split_file_path(file_path):
#
#     dir_path, file_name = os.path.split(file_path)
#     file_name, file_ext = os.path.splitext(file_name)
#
#     return dir_path, file_name, file_ext
#
#
# file_path = "/home/mial/bin/myfile.txt"
# result = split_file_path(file_path)
# print(result)

# ✔Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# names = ['Андрей', "Виктор", "Женя",'Аркадий']
# pays = [10000, 15000, 20000,25000]
# percents = ['50.25%', "20%", "30.6%","65.9%"]
#
# result = {name: pay * (float(percent[:-1]) / 100) for name, pay, percent in zip(names, pays, percents)}
#
# print(result)

# ✔Создайте функцию генератор чисел Фибоначчи
# def fib_gen():
#     num1 = 0
#     num2 = 1
#     while True:
#         yield num1
#         num1, num2 = num2, num1 + num2
#
#
# fibonacci = fib_gen()
#
# for i in range(25):
#     print(next(fibonacci),end='\t')
