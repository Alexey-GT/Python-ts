# a = 42
# print(type(a), id(a))
# print(type(id))
#
# very_bad_programming_style = sum
# print(very_bad_programming_style([1, 2, 3]))


# def main(a):
#     x = 1
#
#     def func(y):
#         nonlocal x
#         x += 100
#         print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
#         return y + 1
#     return x + func(a)
#
# x = 42
# print(f'In main {x = }')
# z = main(x)
# print(f'{x = }\t{z = }')

def max_before_hundred(*args):
    """Return the maximum number not exceeding 100."""
    m = float('-inf')
    print(m)
    for item in args:
        if m < item < 100:
            m = item
    return m


print(max_before_hundred(-42, 66, 73, 99, 256, 0))
