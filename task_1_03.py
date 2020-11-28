'''     lesson_4_hw(task_1_03.py)

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

# Третий вариант, использование цикла while

def array_3(n):
    # def array(MIN_ITEM, MAX_ITEM, SIZE)
    arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)] # создание случайных чисел в 1-м массиве с
    return arr1

def main_3(n):
    arr1 = array_3(n)
    min_el = 0
    max_el = 0
    i = 0

    while i < len(arr1):
        if arr1[i] < arr1[min_el]:
            min_el = i
        if arr1[i] > arr1[max_el]:
            max_el = i
        i += 1
    if min_el > max_el:
        min_el, max_el = max_el, min_el  # изменение положения макс и мин для корректной работы алгоритма

    s = 0
    el = []  # для проверки суммируемых данных
    for i in range(min_el + 1, max_el):
        s += arr1[i]
        el.append(arr1[i])
    n = f'Сумма {el} элементов = {s}'
    return n

# При использовании в цикле while второго 'if'
# print(timeit.timeit('main_3(10)', number=100, globals=globals()))     # 0.0019795590000000023
# print(timeit.timeit('main_3(100)', number=100, globals=globals()))    # 0.017343564
# print(timeit.timeit('main_3(1000)', number=100, globals=globals()))   # 0.17365284
# print(timeit.timeit('main_3(10000)', number=100, globals=globals()))  # 1.6784338749999999
# print(timeit.timeit('main_3(100000)', number=100, globals=globals())) # 16.86281321

# При использовании в цикле while 'elif' вместо второго 'if'
# 0.0019464490000000029
# 0.017289598000000003
# 0.166523582
# 1.6602847790000002
# 16.589936799

# cProfile.run('main_3(10)')
# cProfile.run('main_3(100)')
# cProfile.run('main_3(1000)')
# cProfile.run('main_3(10000)')
# cProfile.run('main_3(100000)')
'''-'''
#       72 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     10    0.000    0.000    0.000    0.000 random.py:244(randint)
#     10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.000    0.000 task_1.py:311(array_3)
#      1    0.000    0.000    0.000    0.000 task_1.py:313(<listcomp>)
#      1    0.000    0.000    0.000    0.000 task_1.py:318(main_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       634 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#    100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#    100    0.000    0.000    0.000    0.000 random.py:244(randint)
#    100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.000    0.000 task_1.py:311(array_3)
#      1    0.000    0.000    0.000    0.000 task_1.py:313(<listcomp>)
#      1    0.000    0.000    0.000    0.000 task_1.py:318(main_3)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    121    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       6403 function calls in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#   1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
#   1000    0.000    0.000    0.002    0.000 random.py:244(randint)
#   1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.002    0.002 task_1.py:311(array_3)
#      1    0.000    0.000    0.002    0.002 task_1.py:313(<listcomp>)
#      1    0.001    0.001    0.003    0.003 task_1.py:318(main_3)
#      1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#   1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    132    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#   1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1264    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       62895 function calls in 0.030 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.030    0.030 <string>:1(<module>)
#  10000    0.007    0.000    0.015    0.000 random.py:200(randrange)
#  10000    0.005    0.000    0.020    0.000 random.py:244(randint)
#  10000    0.006    0.000    0.008    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.024    0.024 task_1.py:311(array_3)
#      1    0.004    0.004    0.024    0.024 task_1.py:313(<listcomp>)
#      1    0.004    0.004    0.030    0.030 task_1.py:318(main_3)
#      1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
#  10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#    115    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#  10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12773    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#       626869 function calls in 0.299 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.299    0.299 <string>:1(<module>)
# 100000    0.075    0.000    0.156    0.000 random.py:200(randrange)
# 100000    0.042    0.000    0.198    0.000 random.py:244(randint)
# 100000    0.057    0.000    0.081    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.242    0.242 task_1.py:311(array_3)
#      1    0.044    0.044    0.242    0.242 task_1.py:313(<listcomp>)
#      1    0.046    0.046    0.299    0.299 task_1.py:318(main_3)
#      1    0.000    0.000    0.299    0.299 {built-in method builtins.exec}
# 100001    0.011    0.000    0.011    0.000 {built-in method builtins.len}
#     46    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 100000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 126816    0.015    0.000    0.015    0.000 {method 'getrandbits' of '_random.Random' objects}
'''-'''

# ============// 3-й тест =============================

# В первом тесте видна линейная зависимость О(n)
#
# Во втором тесте при усложнении, видим медленное выполненние алгоритма О(n**3)
# В данном тесте нарушается филосовия Python в части: "Простое лучше, чем сложное"
#
# В третьем при замене цикла for на while и комбинацией условий 1 - if и 2 - if или 1- if и 2- elif.
# С использованием elif алгоритм работает быстрее, но так же как и в первом тесте прослеживается
# линейная зависимость О(n)
#
# Во всех тестах основное время при работе алгоритмов занимает рандомная генерация списка
