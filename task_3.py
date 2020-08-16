"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
   Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
   Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
   Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
   вашей  ОС.
"""
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.(Пример №1)
from guppy import hpy
from copy import deepcopy

def adder(*nums):
    sum = 0
    for n in nums:
        sum //= n
    print("sum:", sum)


adder(10, 10, 1)

h = hpy()

nums = list(range(100000))
sum = deepcopy(nums)

print(h.heap())

"""
Partition of a set of 133796 objects. Total size = 8340326 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0 100892  75  2825248  34   2825248  34 int
     1    103   0  1642832  20   4468080  54 list
     2   9901   7   887768  11   5355848  64 str
     3   6835   5   476808   6   5832656  70 tuple
     4   2417   2   427488   5   6260144  75 types.CodeType
     5    445   0   343480   4   6603624  79 type
     6   4829   4   341518   4   6945142  83 bytes
     7   2212   2   300832   4   7245974  87 function
     8    445   0   241384   3   7487358  90 dict of type
     9     94   0   172144   2   7659502  92 dict of module
     
Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux

"""

##################################################################################################
# Сформировать из введенного числа обратное по порядку, Решите через рекурсию.(Пример №2)


def reverse_int(s):
    chars = list(s)
    for i in range(len(s) // 2):
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)


data = reverse_int('3486')
print(data)

h = hpy()

s = list(range(100000))
chars = deepcopy(s)

print(h.heap())

"""
Partition of a set of 233492 objects. Total size = 12755655 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0 200601  86  5617100  44   5617100  44 int
     1    105   0  3267344  26   8884444  70 list
     2   9902   4   887821   7   9772265  77 str
     3   6835   3   476808   4  10249073  80 tuple
     4   2417   1   427488   3  10676561  84 types.CodeType
     5    445   0   343480   3  11020041  86 type
     6   4829   2   341518   3  11361559  89 bytes
     7   2213   1   300968   2  11662527  91 function
     8    445   0   241384   2  11903911  93 dict of type
     9     94   0   172144   1  12076055  95 dict of module
     
Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux

"""

###################################################################################################
# Докажите, что словари обрабатываются быстрее, чем списки.(Пример №3)

d = {a: 1 + a for a in range(100)}
print(d)


h = hpy()

d = list(range(100000))
a = deepcopy(d)

print(h.heap())

"""
Partition of a set of 333237 objects. Total size = 17173309 bytes.
 Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
     0 300344  90  8409904  49   8409904  49 int
     1    107   0  4891856  28  13301760  77 list
     2   9902   3   887821   5  14189581  83 str
     3   6835   2   476808   3  14666389  85 tuple
     4   2417   1   427826   2  15094215  88 types.CodeType
     5    445   0   343480   2  15437695  90 type
     6   4829   1   341518   2  15779213  92 bytes
     7   2213   1   300968   2  16080181  94 function
     8    445   0   241384   1  16321565  95 dict of type
     9     94   0   172144   1  16493709  96 dict of module
     
Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux

"""
