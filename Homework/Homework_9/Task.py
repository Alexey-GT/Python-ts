import math
import csv
import random
import csv
import json
# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "Нет корней"


def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

def quadratic_equation_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Equation: {a}x^2 + {b}x + {c} = 0")
                print(f"Roots: {result}")
                print()
    return wrapper

def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "parameters": {
                    "args": args,
                    "kwargs": kwargs
                },
                "result": result
            }
            with open(filename, 'w') as file:
                json.dump(data, file)
            return result
        return wrapper
    return decorator

@quadratic_equation_decorator
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

@save_to_json("result.json")
def some_function(x, y):
    return x + y

find_roots("equations.csv")
result = some_function(3, 4)
print(result)