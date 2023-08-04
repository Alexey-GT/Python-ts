# def func(a):
#     x = 1
#     res = x + a
#     return res
#
# print(func(1))
# x = 188
# print(func(1))

#Замыкание функции
# from typing import Callable
#
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     # names = []
#     def add_two_str(b: str) -> str:
#         names = []
#         names.append(b)
#         return a + ', ' + ', '.join(names)
#
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))

#Декоратор
import time
from typing import Callable
def main(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result
    return wrapper
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
print(f'{factorial(1000) = }')
control = main(factorial)
print(f'{control.__name__ = }')
print(f'{control(1000) = }')