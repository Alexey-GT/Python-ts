import string
from collections import Counter

# Task_8_seminar
# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

# friends = {"Alexey": ('Нож', "Пила", "Ружье", "Самогон", "Патроны", "Вода", "Веревка"),
#           "Андрей": ("Нож", "Топор", "Спички", "Вода", "Веревка"),
#           "Игорь": ("Нож", "Топор", "Вода", "Спички")}
# have_all = set()
# for i in friends.values():
#     have_all |= set(i)
# print(f"У ребят в арсенале: {', '.join(have_all)}")
#
# uniques = set()
# for i in friends:
#     temp = set(friends[i])
#     for j in friends:
#         if j == i:
#             continue
#         temp -= set(friends[j])
#     if temp:
#         print(f"{', '.join(temp)} есть только у {i}")
#     uniques |= temp
#
#
#
# things_count = Counter(sum([list(i) for i in friends.values()], start = []))
# for i in things_count:
#     if things_count[i] == len(friends) - 1:
#         for j in friends:
#             if i not in friends[j]:
#                 print(f"{j} забыл {i}")

# Task_1
# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов

# lst = [1, 4, 1, 6, 4, 7, 5, 3, 4]
# i = 0
# res = []
# while len(lst) > i:
#     if lst.count(lst[i]) >= 2:
#         res.append(lst[i])
#     i += 1
# print(set(res))


# Task_2
# #  В большой текстовой строке подсчитать количество встречаемых
# # слов и вернуть 10 самых частых. Не учитывать знаки препинания
# # и регистр символов. За основу возьмите любую статью
# # из википедии или из документации к языку

# str_other = "ddQEDCDCSDCXC,.. ZxCDLLVKJSKVJKVKMNSmkmck..?:mckkmc njsfhjvkbnopyjnrnmn n"
# str_new = str_other.lower().translate(str.maketrans(' ', ' ', string.punctuation))
# print(str_new)
# dict_1 = {}
# dict_2 = {}
# i = 0
# max = 0
# count = 9
# while len(str_new) > i:
#     if str_new.count(str_new[i]) > 1:
#         dict_1.setdefault(str_new[i], str_new.count(str_new[i]))
#     i += 1
# print(dict_1)
# while 0 <= count:
#     for key, val in dict_1.items():
#         if val > max:
#             max = val
#     dict_2.setdefault(key,val)
#     dict_1.pop(key)
#     count -= 1
# print(dict_2)


# Task_3
# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.