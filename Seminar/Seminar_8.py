# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json
import os

# def file_transform_to_json(filename):
#     with (open(filename, "r", encoding='utf-8') as file1,
#           open(f'{filename}.json', "w", encoding='utf-8') as file2):
#         data = file1.readlines()
#         dict_to_save = {}
#         for line in data:
#             key, value = line.strip().split(" ")
#             if key.title() in dict_to_save.keys():
#                 dict_to_save[key.title()].append(value)
#             else:
#                 dict_to_save[key.title()] = [value]
#         json.dump(dict_to_save, file2, ensure_ascii=False,  indent=2)
#
# filename = "res.txt"
# file_transform_to_json(filename)


# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
# def func():
#
#
#     while True:
#         str_inp = input('Введите данные: ')
#         if str_inp:
#             name, pers_id, level = str_inp.split()
#             level = int(level)
#             if not 0 < int(level) < 8:
#                 print('Давай сначала')
#                 continue
#             with open('my_file.json', 'r') as f:
#                 try:
#                     data = json.load(f)
#                 except:
#                     data = {}
#             if level not in data:
#                 data[level] = {}
#             data[level][pers_id] = name
#             with open('my_file.json', 'w') as f:
#                 json.dump(data, f, indent=2)
#         else:
#             break
# func()



# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
# def func():
#     with (open('my_file.json', 'r') as f1,
#           open('name.csv', 'w', encoding='utf-8', newline='') as file):
#         data = json.load(f1)
#         columns = ['level', 'pers_id', 'name']
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(columns)
#         result = []
#         for key, value in data.items():
#             for i in data[key]:
#                 result.append([key, i, data[key][i]])
#         writer.writerows(result)

# 📌Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌Дополните id до 10 цифр незначащими нулями.
# 📌В именах первую букву сделайте прописной.
# 📌Добавьте поле хеш на основе имени и идентификатора.
# 📌Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# 📌Имя исходного и конечного файлов передавайте как аргументы функции.

# def func(source_file, dest_file):
#     with (open(source_file, 'r') as f1,
#           open(dest_file, 'w', encoding='utf-8') as file):
#         csv_file = csv.reader(f1, delimiter=';')
#         next(csv_file)
#         new_dict = {}
#         for level, pers_id, name in csv_file:
#             pers_id = pers_id.rjust(10, '0')
#             name = name.title()
#             hash_id = hash(name + pers_id)
#             new_dict[hash_id] = {pers_id: [name, level]}
#         json.dump(new_dict, file, indent=2)
#
#
# func('name.csv', 'names.json')

# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
# def rename_file():
#     for file in os.listdir():
#         if file.endswith('.json'):
#             with (open(file, 'r') as file_inp,
#                   open(f'{file[:-5]}.pickle', 'wb') as file_out):
#                 pickle.dump((json.load(file_inp)), file_out)
#
# rename_file()

# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.



# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.
os.walk()