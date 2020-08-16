"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
# Решение профилирование памяти в скриптах:
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.(Пример №1)
from memory_profiler import profile

def adder(*nums):
    sum = 0
    for n in nums:
        sum //= n
    print("sum:", sum)


adder(10, 10, 1)


class Adder:
    def __init__(self, nums=0, n=0, lst=None):
        if lst is None:
            lst = []
        self.nums = nums
        self.n = n
        self.lst = list(range(100000))

    def __del__(self):
        class_name = self.__class__.__name__
        print(f'{class_name} уничтожен')


@profile
def adder():
    pt1 = Adder()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt3))
    del pt1
    del pt2
    del pt3


adder()
"""
140394053715472 140394053715472 140394053715472
    Adder уничтожен
     44     13.3 MiB     13.3 MiB   @profile
     45                             def adder():
     46     17.3 MiB      3.9 MiB       pt1 = Adder()
     47     17.3 MiB      0.0 MiB       pt2 = pt1
     48     17.3 MiB      0.0 MiB       pt3 = pt1
     49     17.3 MiB      0.0 MiB       print(id(pt1), id(pt2), id(pt3))
     50     17.3 MiB      0.0 MiB       del pt1
     51     17.3 MiB      0.0 MiB       del pt2
     52     13.9 MiB      0.0 MiB       del pt3  
     
Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
Adder -  Потребляет меньше всего памяти, но проигрывает по скорости всех остальных функций.                                  
"""
##############################################################################################
# Сформировать из введенного числа обратное по порядку, Решение через рекурсию.(Пример №2)


def reverse_int(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)


data = reverse_int('3486')
print(data)


class Reverse_int:
    def __init__(self, s=0, chars=0, lst=[]):
        self.s = s
        self.chars = chars
        self.lst = list(range(100000))

    def __del__(self):
        class_name = self.__class__.__name__
        print(f'{class_name} уничтожен')


@profile
def reverse_int():
    pt1 = Reverse_int()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt3))
    del pt1
    del pt2
    del pt3


reverse_int()
"""
139735175091536 139735175091536 139735175091536
Reverse_int уничтожен
   100     14.0 MiB     14.0 MiB   @profile
   101                             def reverse_int():
   102     17.3 MiB      3.3 MiB       pt1 = Reverse_int()
   103     17.3 MiB      0.0 MiB       pt2 = pt1
   104     17.3 MiB      0.0 MiB       pt3 = pt1
   105     17.3 MiB      0.0 MiB       print(id(pt1), id(pt2), id(pt3))
   106     17.3 MiB      0.0 MiB       del pt1
   107     17.3 MiB      0.0 MiB       del pt2
   108     14.8 MiB      0.0 MiB       del pt3

Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
Reverse_int - Работает быстро, и потребляет меньше памяти чем Dict.
"""
########################################################################################################

# Докажите, что словари обрабатываются быстрее, чем списки.(Пример №3)

d = {a: 1 + a for a in range(100)}
print(d)



class Dict:
    def __init__(self, d=0, a=0, lst=[]):
        self.lst = lst
        self.d = d
        self.a = a
        self.lst = list(range(100000))

    def __del__(self):
        class_name = self.__class__.__name__
        print(f'{class_name} уничтожен')


@profile
def dict():
    pt1 = Dict()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt3))
    del pt1
    del pt2
    del pt3


dict()
"""
139735175091872 139735175091872 139735175091872
Dict уничтожен
   134     14.8 MiB     14.8 MiB   @profile
   135                             def dict():
   136     17.3 MiB      2.6 MiB       pt1 = Dict()
   137     17.3 MiB      0.0 MiB       pt2 = pt1
   138     17.3 MiB      0.0 MiB       pt3 = pt1
   139     17.3 MiB      0.0 MiB       print(id(pt1), id(pt2), id(pt3))
   140     17.3 MiB      0.0 MiB       del pt1
   141     17.3 MiB      0.0 MiB       del pt2
   142     14.8 MiB      0.0 MiB       del pt3

Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
dict - Работает быстрей, но потребляет больше памяти чем все отстальные функции. 
"""
# Использовал NanPy ну только со словарем, не с массивом.
import numpy as np
import sys
d = {a: 1 + a for a in range(100)}
numpy_arr = np.array({a: 1 + a for a in range(100)})

sizeof_py_arr = sys.getsizeof(1) * len(d)
sizeof_numpy_arr = numpy_arr.itemsize * numpy_arr.size

print(sizeof_py_arr)
print(sizeof_numpy_arr)
print(numpy_arr)

"""
2800
8
{0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33, 33: 34, 34: 35, 35: 36, 36: 37, 37: 38, 38: 39, 39: 40, 40: 41, 41: 42, 42: 43, 43: 44, 44: 45, 45: 46, 46: 47, 47: 48, 48: 49, 49: 50, 50: 51, 51: 52, 52: 53, 53: 54, 54: 55, 55: 56, 56: 57, 57: 58, 58: 59, 59: 60, 60: 61, 61: 62, 62: 63, 63: 64, 64: 65, 65: 66, 66: 67, 67: 68, 68: 69, 69: 70, 70: 71, 71: 72, 72: 73, 73: 74, 74: 75, 75: 76, 76: 77, 77: 78, 78: 79, 79: 80, 80: 81, 81: 82, 82: 83, 83: 84, 84: 85, 85: 86, 86: 87, 87: 88, 88: 89, 89: 90, 90: 91, 91: 92, 92: 93, 93: 94, 94: 95, 95: 96, 96: 97, 97: 98, 98: 99, 99: 100}

"""
######################################################################################################
# NanPy с массивом.

import numpy as np
import sys
from memory_profiler import profile

py_arr = [1,2,3,4,5,6]
numpy_arr = np.array([1,2,3,4,5,6])

sizeof_py_arr = sys.getsizeof(1) * len(py_arr)
sizeof_numpy_arr = numpy_arr.itemsize * numpy_arr.size


class Array:
    def __init__(self, py_arr=0, numpy_arr=0, lst=[]):
        self.lst = lst
        self.py_arr = py_arr
        self.numpy_arr = numpy_arr
        self.lst = list(range(100000))

    def __del__(self):
        class_name = self.__class__.__name__
        print(f'{class_name} уничтожен')


@profile
def array():
    pt1 = Array()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt3))
    del pt1
    del pt2
    del pt3

array()

print(py_arr)
print(numpy_arr)
print(sizeof_py_arr )
print(sizeof_numpy_arr)

"""
[1, 2, 3, 4, 5, 6]
[1 2 3 4 5 6]
168
48
Разница в количестве занятой памяти.

140243860241280 140243860241280 140243860241280
Array уничтожен

    24     29.6 MiB     29.6 MiB   @profile
    25                             def array():
    26     33.4 MiB      3.9 MiB       pt1 = Array()
    27     33.4 MiB      0.0 MiB       pt2 = pt1
    28     33.4 MiB      0.0 MiB       pt3 = pt1
    29     33.4 MiB      0.0 MiB       print(id(pt1), id(pt2), id(pt3))
    30     33.4 MiB      0.0 MiB       del pt1
    31     33.4 MiB      0.0 MiB       del pt2
    32     30.1 MiB      0.0 MiB       del pt3
    
Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
"""