# data = [1, 2.4, True, "str"]
# for i in range(len(data)):
#     print(i + 1)
#     print(id(data[i]))
#     print(data[i].__sizeof__())
#     print(hash(data[i]))
#     print(isinstance(data[i], int))

# ✔Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# ✔Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно: ✔Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔Избегайте магических чисел ✔Добавьте аннотацию типов где это возможно


# num = int(input())
#
# def conv(num, sys):
#     res = list()
#     while num > 0:
#         res.append(str(num % sys))
#         num //= sys
#     return "".join(reversed(res))
# print(conv(3, 2))

# ✔Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔Диаметр не превышает 1000 у.е.
# ✔Точность вычислений должна составлять не менее 42 знаков после запятой.

# ✔Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# ✔Используйте комплексные числа для извлечения квадратного корня.

# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
# 1 ВАРИАНТ
# FEE = 0.015
# INTEREST = 0.03
# TAX = 0.1
#
# balance = 0
# menu = "1 - пополнить, 2 - снять, 3 - выход: "
# run = True
# counter = 0
#
# while run:
#     if balance >= 5000000:
#         balance = balance - balance * TAX
#     if counter == 3:
#         counter = 0
#         balance = balance * INTEREST + balance
#     print(f'баланс {balance}')
#     match input(menu):
#         case '1':
#             num = int(input("введите сумму для пополнения: "))
#             if num % 50 != 0:
#                 print("сумма должна быть кратна 50")
#                 continue
#             balance += num
#             counter += 1
#         case '2':
#             num = int(input("введите сумму для снятия: "))
#             if num % 50 != 0:
#                 print("сума должна быть кратна 50")
#                 continue
#             num = num + 30 if num * FEE <= 30 else num + 600 if num * FEE >= 600 else num * FEE + num
#             if num > balance:
#                 print('сумма  превышает баланс')
#                 continue
#             balance -= num
#             counter += 1
#         case '3':
#             run = False
#         case _:
#             print("ошибка ввода")
#2ВАРИАНТ------------------------------------------------------------------------------------------------
# total_cash = 0
# count = 0
# while True:
#
#     if total_cash > 5_000_000:
#         total_cash *= 0.9
#
#     print("сумма на счете ", total_cash)
#
#     print("1 - пополнить")
#     print("2 - снять")
#     print("0 - выйти")
#
#     action = input("введите номер операции: ")
#
#
#     match action:
#         case "1":
#             add = int(input("внесите сумму кратную 50: "))
#             if add % 50 == 0:
#                 total_cash += add
#                 count += 1
#             else:
#                 print("неверная сумма")
#
#         case "2":
#             take = int(input("введите сумму снятия кратную 50: "))
#             if take % 50 == 0:
#                 percent = take*1.5*0.01
#                 if percent < 30 :
#                     percent = 30
#                 if percent > 600:
#                     percent = 600
#
#                 if total_cash < (take+percent):
#                     print("недостаточно средств")
#                 else:
#                     total_cash -= (take+percent)
#                     count += 1
#             else:
#                 print("неверная сумма")
#
#         case "0":
#             quit()
#
#     if count == 3:
#         total_cash *= 1.03
#         count = 0