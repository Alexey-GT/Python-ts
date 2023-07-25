# import random as rnd
# from sys import builtin_module_names as bmn, path as p
# print(bmn)
# print(*p, sep='\n')
# print(rnd.randint(1, 6))
# print(path) # NameError: name 'path' is not defined
# print(sys.path) # NameError: name 'sys' is not defined
"""Four basic mathematical operations.
Addition, subtraction, multiplication and division as functions.
"""
# _START_SUM = 0
# _START_MULT = 1
# _BEGINNING = 0
# _CONTINUATION = 1
#
#
# def add(*args):
#
#
#     res = _START_SUM
# for item in args:
#     res += item
# 12
#     return res
#
#
# def sub(*args):
#
#
#     res = args[_BEGINNING]
# for item in args[_CONTINUATION:]:
#     res -= item
# return res
#
#
# def mul(*args):
#
#
#     res = _START_MULT
# for item in args:
#     res *= item
# return res
#
#
# def div(*args):
#
#
#     res = args[_BEGINNING]
# for item in args[_CONTINUATION:]:
#     res /= item
# return res
