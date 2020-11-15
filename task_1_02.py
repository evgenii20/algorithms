'''     lesson_4_hw(task_1_02.py)

Ур. 3, задача 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Самый минимальный и максимальный элементы в сумму не включать.'''

import cProfile
import timeit
import random

# SIZE = 10  # Размер массива
MIN_ITEM = 0  # Минимальное значение
MAX_ITEM = 100  # максимальное значение
# MIN_ITEM, MAX_ITEM, SIZE
# main(10)

# Второй вариант, усложнил алгоритм, добавил генераторы и функции min и max
def array_2(n):
    # def array(MIN_ITEM, MAX_ITEM, SIZE)
    arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    # создание случайных чисел в 1-м массиве с
    return arr1


def main_2(n):
    # arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создание случайных чисел в 1-м массиве с
    # arr1 = array_2(n)
    min_el = 0
    max_el = 0
    min_el = min([i for i in range(1, len(array_2(n))) if array_2(n)[i] < array_2(n)[min_el]])
    # if arr1[i] < arr1[min_el]:
    #     min_el = i
    max_el = max([i for i in range(1, len(array_2(n))) if array_2(n)[i] > array_2(n)[max_el]])
    # elif arr1[i] > arr1[max_el]:
    # max_el = i
    # print(f'Минимальный элемент {arr1[min_el]}, максимальный элемент {arr1[max_el]}')
    if min_el > max_el:
        min_el, max_el = max_el, min_el  # изменение положения макс и мин для корректной работы алгоритма

    s = 0
    el = []  # для проверки суммируемых данных
    for i in range(min_el + 1, max_el):
        s += array_2(n)[i]
        el.append(array_2(n)[i])
    n = f'Сумма {el} элементов = {s}'
    return n

# print(timeit.timeit('main_2(10)', number=100, globals=globals()))     # 0.06533535100000001
# print(timeit.timeit('main_2(100)', number=100, globals=globals()))    # 7.4564482309999995
# print(timeit.timeit('main_2(1000)', number=100, globals=globals()))   # 751.955647171
# print(timeit.timeit('main_2(10000)', number=100, globals=globals()))  # нет данных
# print(timeit.timeit('main_2(100000)', number=100, globals=globals())) # нет данных

# cProfile.run('main_2(10)')
# cProfile.run('main_2(100)')
# cProfile.run('main_2(1000)')
# cProfile.run('main_2(10000)')
# cProfile.run('main_2(100000)')
'''-'''
#        2897 function calls in 0.001 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     520    0.000    0.000    0.001    0.000 random.py:200(randrange)
#     520    0.000    0.000    0.001    0.000 random.py:244(randint)
#     520    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      52    0.000    0.000    0.001    0.000 task_1.py:175(array_2)
#      52    0.000    0.000    0.001    0.000 task_1.py:177(<listcomp>)
#       1    0.000    0.000    0.001    0.001 task_1.py:182(main_2)
#       1    0.000    0.000    0.000    0.000 task_1.py:187(<listcomp>)
#       1    0.000    0.000    0.001    0.001 task_1.py:190(<listcomp>)
#       1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#       7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     520    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     696    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#        311143 function calls in 0.148 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.148    0.148 <string>:1(<module>)
#   58800    0.047    0.000    0.096    0.000 random.py:200(randrange)
#   58800    0.026    0.000    0.122    0.000 random.py:244(randint)
#   58800    0.035    0.000    0.049    0.000 random.py:250(_randbelow_with_getrandbits)
#     588    0.001    0.000    0.148    0.000 task_1.py:175(array_2)
#     588    0.026    0.000    0.147    0.000 task_1.py:177(<listcomp>)
#       1    0.000    0.000    0.148    0.148 task_1.py:182(main_2)
#       1    0.000    0.000    0.049    0.049 task_1.py:187(<listcomp>)
#       1    0.000    0.000    0.053    0.053 task_1.py:190(<listcomp>)
#       1    0.000    0.000    0.148    0.148 {built-in method builtins.exec}
#       2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      95    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#   58800    0.006    0.000    0.006    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   74662    0.009    0.000    0.009    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#        31566905 function calls in 14.550 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000   14.550   14.550 <string>:1(<module>)
# 5990000    4.572    0.000    9.481    0.000 random.py:200(randrange)
# 5990000    2.540    0.000   12.022    0.000 random.py:244(randint)
# 5990000    3.417    0.000    4.910    0.000 random.py:250(_randbelow_with_getrandbits)
#    5990    0.009    0.000   14.538    0.002 task_1.py:175(array_2)
#    5990    2.508    0.000   14.529    0.002 task_1.py:177(<listcomp>)
#       1    0.004    0.004   14.550   14.550 task_1.py:182(main_2)
#       1    0.004    0.004    4.884    4.884 task_1.py:187(<listcomp>)
#       1    0.004    0.004    4.862    4.862 task_1.py:190(<listcomp>)
#       1    0.000    0.000   14.550   14.550 {built-in method builtins.exec}
#       2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#     996    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 5990000    0.580    0.000    0.580    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 7593919    0.913    0.000    0.913    0.000 {method 'getrandbits' of '_random.Random' objects}

'''-'''
# ============// 2-й тест =============================

