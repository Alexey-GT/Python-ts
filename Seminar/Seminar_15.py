# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.
import logging
#
# logging.basicConfig(level=logging.CRITICAL, filename='loger.log', filemode='a',
#                     format='%(asctime)s, %(levelname)s, %(message)s')
#
# x, y = map(int, input('Введите два целых числа через пробел: ').split())
# try:
#     print((x / y))
#     logging.info('Ok')
# except:
#     logging.error('ZeroDivisionZero')

# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.
# x, y = map(int, input('Введите два целых числа через пробел: ').split())
# def log_deco(func):
#     def wrapper(x, y):
#         try:
#             logging.info(f'Result: {x} / {y} = {func(x, y)}')
#         except:
#             logging.error('ZeroDivisionZero')
#     return wrapper
#
# @log_deco
# def log_div(x, y):
#     return (x / y)
#
# log_div(x, y)

# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.
# logging.basicConfig(filename='log.log',
#                     encoding='utf-8',
#                     format='{name}: {asctime} {levelname} {lineno} -> {msg}',
#                     style='{',
#                     level=logging.INFO)
#
#
# x, y = map(int, input('Введите два целых числа через пробел: ').split())
#
#
# def log_deco(func):
#     def wrapper(x, y):
#         try:
#             logging.info(f'Func {func.__name__} Args: {x}  {y} Res: {func(x, y)}')
#         except:
#             logging.error('ZeroDivisionZero')
#
#     return wrapper
#
#
# @log_deco
# def log_div(x, y):
#     return x / y
#
# @log_deco
# def log_mult(x, y):
#     return x * y
# log_div(x, y)
# log_mult(x, y)


# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
# import re
# import locale
# import logging
# from datetime import date
# from datetime import timedelta
#
# locale.setlocale(locale.LC_ALL, "Russian")
#
#
# def parse_date(string):
#     try:
#         weekdays = {
#             'понедельник': 0,
#             "вторник": 1,
#             "среда": 2,
#             "четверг": 3,
#             "пятница": 4,
#             "суббота": 5,
#             "воскресенье": 6,
#         }
#         months = {'января': 1,
#                   'февраля': 2,
#                   'марта': 3,
#                   'апреля': 4,
#                   'мая': 5,
#                   'июня': 6,
#                   'июля': 7,
#                   'августа': 8,
#                   'сентября': 9,
#                   'октября': 10,
#                   'ноября': 11,
#                   'декабря': 12
#                   }
#
#         day_no = int(re.findall(r'\d+', string)[0])
#         _weekday = weekdays[string.split()[1]]
#         _months = months[string.split()[2]]
#
#         startdate = date(2023, _months, 1)
#         weekday_count = 0
#         while weekday_count < day_no:
#
#             if startdate.weekday() == _weekday:
#                 weekday_count += 1
#             startdate += timedelta(days=1)
#         return startdate - timedelta(days=1)
#     except Exception as e:
#         logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
#                             format='%(levelname)s, %(asctime)s, %(message)s')
#         logging.error(e)
#
#
# print(parse_date(input('>>>')))

# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.
# import re
# import locale
# import logging
# from datetime import date
# from datetime import timedelta
#
# locale.setlocale(locale.LC_ALL, "Russian")
# logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
#                     format='%(levelname)s, %(asctime)s, %(message)s')
#
#
# def parse_date(string):
#     string = ' '.join(string)
#     try:
#         weekdays = {
#             'понедельник': 0,
#             "вторник": 1,
#             "среда": 2,
#             "четверг": 3,
#             "пятница": 4,
#             "суббота": 5,
#             "воскресенье": 6,
#         }
#         months = {'января': 1,
#                   'февраля': 2,
#                   'марта': 3,
#                   'апреля': 4,
#                   'мая': 5,
#                   'июня': 6,
#                   'июля': 7,
#                   'августа': 8,
#                   'сентября': 9,
#                   'октября': 10,
#                   'ноября': 11,
#                   'декабря': 12
#                   }
#
#         day_no = int(re.findall(r'\d+', string)[0])
#         _weekday = weekdays[string.split()[1]]
#         _months = months[string.split()[2]]
#
#         startdate = date(2023, _months, 1)
#         weekday_count = 0
#         while weekday_count < day_no:
#             if startdate.weekday() == _weekday:
#                 weekday_count += 1
#             startdate += timedelta(days=1)
#         logging.info(startdate - timedelta(days=1))
#         return startdate - timedelta(days=1)
#     except Exception as e:
#         logging.error(e)
#
#
# import argparse
#
# # str_inp = '4-ый четверг ноября'
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Логер даты.')
#     parser.add_argument('-a', type=str, nargs=1, help='Введите порядковый день недели', default=['1'])
#     parser.add_argument('-b', type=str, nargs=1, help='Текущий день недели', default=['вторник'])
#     parser.add_argument('-c', type=str, nargs=1, help='Текущий месяц', default=['августа'])
#     args = parser.parse_args()
#     args_list = args.a + args.b + args.c
#     print(args_list)
#     print(parse_date(args_list))

# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.
# import locale
# import logging
# from collections import namedtuple
#
# locale.setlocale(locale.LC_ALL, "Russian")
#
#
# logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
#                         format='%(levelname)s, %(asctime)s, %(message)s')
#
# def file_listening(path='.'):
#     """
#     Рекурсивно обходит заданный каталог и все вложенные директории
#     """
#
#     for dirpath, dir_name, file_name in os.walk(path):
#         Files = namedtuple('Files', ['item_name', 'file_ext', 'dir_flag', 'parent_path'])
#         parent_path = dirpath.split('\\')[-2]
#
#         if dir_name:
#             dir_flag = 'Is a direcory.'
#             exp_dict = Files(dir_name, None, dir_flag, parent_path)
#             logging.info(f'{exp_dict}')
#
#         if file_name:
#             dir_flag = 'Is a file.'
#             for f in file_name:
#                 exp_dict = Files(f.split('.')[0], f.split('.')[-1], dir_flag, parent_path)
#                 logging.info(f'{exp_dict}')
#
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Сканер файлов.')
#     parser.add_argument('path', type=str, help='Введите путь: ', default=os.getcwd())
#     args = parser.parse_args()
#     print(file_listening(args.path))