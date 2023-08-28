from loguru import logger #Установил новый модуль loguru
import argparse
class TriangleChecker:
    """Внутри класса идет логгирование и запись логов в файл"""
    def __init__(self, a: int, b: int, c: int) -> None:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            logger.error('Only int or float numbers allowed')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG', rotation='10:00')
            raise TypeError('Only int or float numbers allowed')
        elif a > c + b or b > a + c or c > b + a:
            logger.error('No triangle with these sides is possible')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG', rotation='10:00')
            raise ValueError('No triangle with these sides is possible')
        else:
            self.a = a
            self.b = b
            self.c = c
            logger.info('This triangle can exist')
            logger.add('craft.log', format='{time}, {level}, {message}', rotation='10:00')
    def get_sides(self):
        return self.a, self.b, self.c
    def is_isosceles(self) -> str:
        """Проверка на равнобедренность"""
        if (self.a == self.b and self.b != self.c and self.a != self.c) or (
                self.c == self.b and self.b != self.a and self.c != self.a):
            logger.info('Triangle is isosceles')
            logger.add('craft.log', format='{time}, {level}, {message}', rotation='10:00')
            return f'Triangle is isosceles'
        else:
            logger.error('Triangle is not isosceles')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG', rotation='10:00')
            return f'Triangle is not isosceles'
    def is_equilateral(self) -> str:
        """Проверка на равносторонность"""
        if self.a == self.b == self.c:
            logger.info('Triangle is equilateral')
            logger.add('craft.log', format='{time}, {level}, {message}', rotation='10:00')
            return f'Triangle is equilateral'
        else:
            logger.error('Triangle is not equilateral')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG', rotation='10:00')
            return f'Triangle is not equilateral'
    @staticmethod
    def do_parsing():
        parser = argparse.ArgumentParser(description='hometask_final')
        parser.add_argument('-p', metavar='path', type=str, nargs='*', default='|', help='Put your path here')
        args = parser.parse_args()
        return args.p
hh=TriangleChecker(1,2,2)