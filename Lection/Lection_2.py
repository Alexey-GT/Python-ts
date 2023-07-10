import math
# print(dir("Hello world!"))
# help("Hello world!")
# help(str)
# help()

# x = int("42")
# y = int(3.1415)
# z = int("hello", base=30)
# print(x, y, z, sep='\n')

# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP


# DEFAULT = 42
# num = int(input('Введите уровень или ноль для значения поумолчанию: '))
# level = num or DEFAULT
# print(level)

# LIMIT = 120
# ATTENTION = 'Внимание!'
# name = input('Твоё имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) + \
#        " до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
# print(text)

# empty_str = ''
# en_str = 'Text'
# ru_str = 'Текст'
# unicode_str = '😀😍😉🙃'
# print(empty_str.__sizeof__())
# print(en_str.__sizeof__())
# print(ru_str.__sizeof__())
# print(unicode_str.__sizeof__())
# print(unicode_str)

help(math.gcd())
