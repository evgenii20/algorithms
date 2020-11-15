'''     lesson_4_hw(task_1_01.py)
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

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

# Первый вариант, создание массива вынесено в отдельнуою функцию
def array(n):
    # def array(MIN_ITEM, MAX_ITEM, SIZE)
    arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]  # создание случайных чисел в 1-м массиве с
    return arr1


def main(n):
    # arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создание случайных чисел в 1-м массиве с
    arr1 = array(n)
    min_el = 0
    max_el = 0
    for i in range(1, len(arr1)):
        if arr1[i] < arr1[min_el]:
            min_el = i
        elif arr1[i] > arr1[max_el]:
            max_el = i
    # print(f'Минимальный элемент {arr1[min_el]}, максимальный элемент {arr1[max_el]}')
    if min_el > max_el:
        min_el, max_el = max_el, min_el  # изменение положения макс и мин для корректной работы алгоритма

    s = 0
    el = []  # для проверки суммируемых данных
    for i in range(min_el + 1, max_el):
        s += arr1[i]
        el.append(arr1[i])
    # print(el)
    # print(f'Сумма {el} элементов = {s}')
    n = f'Сумма {el} элементов = {s}'
    return n

# print(timeit.timeit('main(10)', number=100, globals=globals()))     # 0.0018179770000000019
# print(timeit.timeit('main(100)', number=100, globals=globals()))    # 0.016165462000000002
# print(timeit.timeit('main(1000)', number=100, globals=globals()))   # 0.15351659899999998
# print(timeit.timeit('main(10000)', number=100, globals=globals()))  # 1.513171147
# print(timeit.timeit('main(100000)', number=100, globals=globals())) # 15.226786607

# cProfile.run('main(10)')
# cProfile.run('main(100)')
# cProfile.run('main(1000)')
# cProfile.run('main(10000)')
# cProfile.run('main(100000)')
'''-'''

#       61 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     10    0.000    0.000    0.000    0.000 random.py:244(randint)
#     10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.000    0.000 task_1.py:17(array)
#      1    0.000    0.000    0.000    0.000 task_1.py:19(<listcomp>)
#      1    0.000    0.000    0.000    0.000 task_1.py:22(main)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       539 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#    100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#    100    0.000    0.000    0.000    0.000 random.py:244(randint)
#    100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.000    0.000 task_1.py:17(array)
#      1    0.000    0.000    0.000    0.000 task_1.py:19(<listcomp>)
#      1    0.000    0.000    0.000    0.000 task_1.py:22(main)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    129    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#

#
#       5492 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#   1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
#   1000    0.000    0.000    0.002    0.000 random.py:244(randint)
#   1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.003    0.003 task_1.py:17(array)
#      1    0.000    0.000    0.003    0.003 task_1.py:19(<listcomp>)
#      1    0.000    0.000    0.003    0.003 task_1.py:22(main)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    216    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#   1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1269    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       53331 function calls in 0.027 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.027    0.027 <string>:1(<module>)
#  10000    0.008    0.000    0.016    0.000 random.py:200(randrange)
#  10000    0.004    0.000    0.020    0.000 random.py:244(randint)
#  10000    0.006    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.024    0.024 task_1.py:17(array)
#      1    0.005    0.005    0.024    0.024 task_1.py:19(<listcomp>)
#      1    0.003    0.003    0.027    0.027 task_1.py:22(main)
#      1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    561    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12763    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       526877 function calls in 0.271 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.271    0.271 <string>:1(<module>)
# 100000    0.076    0.000    0.159    0.000 random.py:200(randrange)
# 100000    0.042    0.000    0.201    0.000 random.py:244(randint)
# 100000    0.057    0.000    0.082    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.246    0.246 task_1.py:17(array)
#      1    0.045    0.045    0.246    0.246 task_1.py:19(<listcomp>)
#      1    0.025    0.025    0.271    0.271 task_1.py:22(main)
#      1    0.000    0.000    0.271    0.271 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    264    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 100000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 126606    0.015    0.000    0.015    0.000 {method 'getrandbits' of '_random.Random' objects}
'''-'''
# ============// 1-й тест =============================
