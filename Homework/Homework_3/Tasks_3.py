import string

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
dict_things = {"Нож": 2, "Компас": 0.2, "Патроны": 3, "Сигнальная ракета": 3, "Ружье": 5, "Виски": 1}
max_weight = 5