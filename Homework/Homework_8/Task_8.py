# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import os
import json
import csv
import pickle


def travers_directory(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            result.append({
                'path': file_path,
                'type': 'file',
                'size': file_size
            })
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_directory_size(dir_path)
            result.append({
                'path': dir_path,
                'type': directory,
                'size': dir_size
            })
    return result


def get_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
        return total_size


def save_as_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


def save_as_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['path', 'type', 'size'])
        writer.writeheader()
        writer.writerows(data)


def save_as_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


directory = ' '
result = travers_directory(directory)

save_as_json(result, 'result.json')
save_as_csv(result, 'result.csv')
save_as_pickle(result, 'result.pickle')
