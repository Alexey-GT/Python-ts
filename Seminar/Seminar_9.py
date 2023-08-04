from random import randint
#Task_1
# 📌Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○от 1 до 100 для загадывания, ○от 1 до 10 для количества попыток
# 📌Функция возвращает функцию, которая через консоль просит угадать
# загаданное число за указанное число попыток.
# from random import randint
#
# def main():
#     upper_limit, find_try = int(input('Предел? ')), int(input('Попыток?  '))
#
#     def try_to_guess():
#         lower_limit = 1
#         num = randint(lower_limit, upper_limit)
#         print(f'Угадай число от {lower_limit} до {upper_limit}.\n')
#         nonlocal find_try
#         tmp = find_try
#
#         while find_try > 0:
#             guess_try = int(input('Введи число: '))
#             find_try -= 1
#             if guess_try < num:
#                 print('У меня больше.')
#             if guess_try > num:
#                 print('У меня меньше.')
#             if guess_try == num:
#                 print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
#         else:
#             print(f'\nНе угадал! Я загадал {num}.')
#     return try_to_guess
#
#
#
# a = main()
# a()
#Task_2
# 📌Дорабатываем задачу 1.
# 📌Превратите внешнюю функцию в декоратор.
# 📌Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# 📌Если не входят, вызывать функцию со случайными числами из диапазонов.

#
# def main(func):
#     def wrapper(upper_limit, find_try):
#         if not 0 < upper_limit < 100:
#             upper_limit = randint(1, 100)
#         if not 0 < find_try < 10:
#             find_try = randint(1, 10)
#         func(upper_limit, find_try)
#     return wrapper
#
# @main
# def try_to_guess(upper_limit, find_try):
#     num = randint(1, upper_limit)
#     print(f'Угадай число от 1 до {upper_limit}.\n')
#     tmp = find_try
#     while find_try > 0:
#         guess_try = int(input('Введи число: '))
#         find_try -= 1
#         if guess_try < num:
#             print('У меня больше.')
#         if guess_try > num:
#             print('У меня меньше.')
#         if guess_try == num:
#             print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
#     else:
#         print(f'\nНе угадал! Я загадал {num}.')
#
#
#
# try_to_guess(10, 500)

#Task_3
# 📌Напишите декоратор, который сохраняет в json файл параметры декорируемой функции
# и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌Имя файла должно совпадать с именем декорируемой функции.
# def json_saver(func):
#     def wrapper(*args, **kwargs):
#         with open(f'{func.__name__}.json', 'a') as file:
#             temp_dict = {'args' : args}
#             temp_dict.update(kwargs)
#             result = func(*args, **kwargs)
#             temp_dict['result'] =  result
#             json.dump(temp_dict, file, indent=3, ensure_ascii=False)
#         return result
#     return wrapper
#
#
# with open('example.json', 'r') as file:
#     data = json.load(file)
#     print(data)

# Task_4
# 📌Создайте декоратор с параметром.
# 📌Параметр - целое число, количество запусков декорируемой функции.
# def call_count(num):
#     def decorator(func):
#         result = []
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 result.append(func(*args, **kwargs))
#             return result
#         return wrapper
#     return decorator
#
#
# @call_count(5)
# def printer(string):
#     print(string)
#     return 'ok'
#
# print(printer('сработало!'))


# Task_5
# 📌Объедините функции из прошлых задач.
# 📌Функцию угадайку задекорируйте: ○декораторами для сохранения параметров,
# ○декоратором контроля значений и ○декоратором для многократного запуска.
# 📌Выберите верный порядок декораторов.
# @call_count(3)
# @value_control
# @json_saver
# def try_to_guess(upper_limit, find_try):
#     num = randint(1, upper_limit)
#     print(f'Угадай число от 1 до {upper_limit}.\n')
#     tmp = find_try
#     while find_try > 0:
#         guess_try = int(input('Введи число: '))
#         find_try -= 1
#         if guess_try < num:
#             print('У меня больше.')
#         if guess_try > num:
#             print('У меня меньше.')
#         if guess_try == num:
#             print(f'\nТы угадал за {tmp - find_try} попыток! Число {num}.')
#     else:
#         print(f'\nНе угадал! Я загадал {num}.')
#
# try_to_guess(50, 3)