'''     lesson_4_hw_2
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого
числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот
код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:

sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2'''

import cProfile
import timeit

'''Функция нахождения простого числа 
Первый — с помощью алгоритма «Решето Эратосфена».'''


# sieve - решето
def sieves(n):
    # n = 1000
    # r = []
    tmp = []
    sieve = [i for i in range(n ** 2 + 5)]
    sieve[1] = 0  # 1-е число не является простым
    # print(sieve)

    i = 2
    while i < len(sieve):  # Пробегаем по списку и
        if sieve[i] > 0:
            p = i + i
            while p < len(sieve):
                sieve[p] = 0
                p += i
        if sieve[i] != 0:
            tmp.append(sieve[i])
        i += 1

    j = 1  # начинаем с 1-го элемента
    for j in range(1, len(tmp)):
        # for k in range(len(tmp[j])):
        if j == n:
            return f'Вы ввели {n}, простое число {tmp[j - 1]}'


# n = int(input('Введите натуральное число: '))
# print(sieves(n))

# Тест первый
# print(timeit.timeit('sieves(10)', number=100, globals=globals()))     # 0.0072255570000000005
# print(timeit.timeit('sieves(100)', number=100, globals=globals()))    # 0.9798890210000001
# print(timeit.timeit('sieves(1000)', number=100, globals=globals()))   # 108.474821795

# cProfile.run('sieves(10)')
# cProfile.run('sieves(100)')
# cProfile.run('sieves(1000)')

'''-'''
#        315 function calls in 0.000 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 task_2.py:30(sieves)
#       1    0.000    0.000    0.000    0.000 task_2.py:34(<listcomp>)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     283    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      27    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#        35549 function calls in 0.015 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#       1    0.011    0.011    0.015    0.015 task_2.py:30(sieves)
#       1    0.000    0.000    0.000    0.000 task_2.py:34(<listcomp>)
#       1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#   34315    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#    1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#        3932226 function calls in 1.747 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.007    0.007    1.747    1.747 <string>:1(<module>)
#       1    1.289    1.289    1.739    1.739 task_2.py:30(sieves)
#       1    0.055    0.055    0.055    0.055 task_2.py:34(<listcomp>)
#       1    0.000    0.000    1.747    1.747 {built-in method builtins.exec}
# 3853722    0.387    0.000    0.387    0.000 {built-in method builtins.len}
#   78499    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''-'''
#
# ============// Тест первый ============================

'''Функция нахождения простого числа 
Второй — без использования «Решета Эратосфена».'''


def func(num):
    # определяем базовый случай n == 1, вернём 2
    if num == 1:
        return 2
    # вспомогательный массив
    tmp = []
    # эмулируем словарь в цикле c увеличением в 2 раза
    for i in range(2, num ** 2):
        # установим вспомогательный флаг со значением по умолчанию = 0
        chk = 0
        # пробегаем по каждому элементу
        for j in range(2, i):
            # если i % j == 0, то
            if i % j == 0:
                # флаг увеличиваем на 1
                chk += 1
        # если флаг == 0, то
        if chk == 0:
            # записываем в вспомогательный массив число
            tmp.append(i)
            # если длинна массива == n, то прерываем цикл
            if len(tmp) == num:
                break
    # возвращаем резултат командой '.pop()' при удалении последнего элемента
    return tmp.pop()


# num = int(input('Введите натуральное число: '))
# print(sieves(num))

# Тест второй
# print(timeit.timeit('func(10)', number=100, globals=globals()))     # 0.004506703000000001
# print(timeit.timeit('func(100)', number=100, globals=globals()))    # 1.159513175
# print(timeit.timeit('func(1000)', number=100, globals=globals()))   # 331.20202358

#
# cProfile.run('func(10)')
# cProfile.run('func(100)')
# cProfile.run('func(1000)')


#       25 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_2.py:118(func)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
#
#
#       205 function calls in 0.013 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#      1    0.013    0.013    0.013    0.013 task_2.py:118(func)
#      1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#    100    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
#
#
#       2005 function calls in 3.294 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    3.294    3.294 <string>:1(<module>)
#      1    3.293    3.293    3.294    3.294 task_2.py:118(func)
#      1    0.000    0.000    3.294    3.294 {built-in method builtins.exec}
#   1000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#   1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}


'''В первом тесте видим медленное выполнение О(n**2).
 Во втором, так же видим медленное выполнение алгоритма О(n**3).
 Как в первом так и во втором случае основное время тратится на вычисление длинны списка влияющее на 
 выполнение всего алгоритма.
 '''