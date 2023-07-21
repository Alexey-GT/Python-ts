
# Task_1
# Напишите функцию для транспонирования матрицы
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# for k in matrix:
#     for m in k:
#         print(m, end='\t')
#     print()
# print("Трансплонированная матрица")
#
#
#
# def transposition(matrix):
#     for i in range(len(matrix)):
#         for j in range(i + 1, len(matrix)):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
#     for r in matrix:
#         for x in r:
#             print(x, end='\t')
#         print()
#
#
# print(transposition(matrix))
# Task_2
# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


# def dictionary(*,key, value):
#     try:
#         d = {}
#         a = hash(key)
#         d.setdefault(key, value)
#         return d
#     except TypeError:
#         print("Введите не изменяемый тип данных в качестве ключа")
#
#
# print(dictionary(key=1, value=333))
# Task_3
# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


# while True:
#     wallet = 1500
#     currency = 'rub'
#     name_wallet = 'Уважаемый клиент '
#     def cash_withdrawal(money_for_cash: int, wallets: int):
#         global wallet
#         if money_for_cash < 100:
#             return 'Сумма снятия должна быть кратна сумме 100 рублей'
#         if wallet < money_for_cash:
#             return 'Сумма снятия наличных превышает сумму доступного!'
#         else:
#             wallet -= money_for_cash
#             return wallet
#
#
#     def cash_depositing(count: int):
#         global wallet
#         money = int(input('Введите сумму пополнения: '))
#         count = count + money
#         return count
#
#     def switch_case():
#         global wallet
#         way = int(input("Выберите какую операцию вы бы хотели произвести:\n1 ---> "
#                         "Снятие наличных\n2 ---> Внесение средств на картрасчет:\n"))
#         match way:
#             case 1:
#                 print(cash_withdrawal(int(input('Введите сумму для снятия наличных ')), wallet))
#                 print(f'Ваш остаток на счету {name_wallet} {wallet} {currency}')
#                 return
#             case 2:
#                 print(cash_depositing(wallet))
#                 print(f'Ваш остаток на счету {wallet} {currency}')
#
#     switch_case()
