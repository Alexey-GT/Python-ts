# class Person:
#
#     max_up = 3
# p1 = Person()
# print(p1.max_up)
# print(Person.max_up)

# class Person:
#     max_up = 3
#
#
# p1 = Person()
# p2 = Person()
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# p1.max_up = 12
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
# Person.max_up = 42
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')

# class Person:
#     max_up = 3
#
#     def __init__(self):
#         self.level = 1
#         self.health = 100
#
#
# p1 = Person()
# p2 = Person()
# print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
# print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health =}')  # AttributeError: type object 'Person' has no attribute 'level'
# Person.level = 100
# print(f'{Person.level = }, {p1.level = }, {p2.level = }')


# class Person:
#     max_up = 3
#
#
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#
#
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.name = }, {p1.race = }')
# print(f'{p2.name = }, {p2.race = }')
# 9
# print(f'{p3.name = }, {p3.race = }')


# class Person:
#     max_up = 3
#
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#
#     def level_up(self):
#         self.level += 1
#
#
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')
# p3.level_up()
# p1.level_up()
# p3.level_up()
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')

# class User:
#     count = []
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
# u1 = User('One', '123-45-67')
# u2 = User('NoOne', '76-54-321')
# u1.count.append(42)
# u1.count.append(73)
# u2.counter = 256
# u2.count.append(u2.counter)
# u2.count.append(u1.count[-1])
# print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# print(f'{u2.name = }, {u2.phone = }, {u2.count = }')
