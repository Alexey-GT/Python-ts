# a, *b, c = input("Три символа: ")
# print(f'{a=} {b=} {c=}')
# data = (10, "9", 8, 1, 6, 3)
# data1 = data + (22,)
# a, b, c, *d, e = data1
# print(a, b, c, d, e)


# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(list_iter)
# print(*list_iter)


# a = range(0, 10, 2)
# print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')

# my_gen = (chr(i) for i in range(97, 123))
# print(my_gen)
# for char in my_gen:
#     print(char, end="\t")
#

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# res = list(mult)
# print(f'{len(res)=}\n{res}')