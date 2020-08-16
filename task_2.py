"""
Задание 2.
Предложить варианты оптимизации и доказать (наглядно, кодом) их эффективность
"""

import sys

class Point:
    __slots__ = 'x', 'y', 'z'

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

ob = Point(1,2,3)
print(sys.getsizeof(ob))
"""
Задать ограниченный набор атрибутов, которыми будет обладать экземпляр класса.
56
"""

def generate_numbers():
    n: int = 0
    while n < 3:
        yield n
        n += 1

numbers = generate_numbers()
type(numbers)
print(generate_numbers())

"""
Генератор выглядит как функция, но использует вместо return ключевое слово yield.
<generator object generate_numbers at 0x7f6c5f15b820>

"""