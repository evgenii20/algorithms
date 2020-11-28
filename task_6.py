'''
    less_3_hw_6
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Сами минимальный и максимальный элементы в сумму не включать.
'''

import random

SIZE = 10 # Размер массива
MIN_ITEM = 0    # Минимальное значение
MAX_ITEM = 100  # максимальное значение
# EL = 50    # отрицательные числа от 0 до 50

arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создание случайных чисел в 1-м массиве с
print(arr1)

min_el = 0
max_el = 0
for i in range(1, len(arr1)):
    if arr1[i] < arr1[min_el]:
        min_el = i
    elif arr1[i] > arr1[max_el]:
        max_el = i
print(f'Минимальный элемент {arr1[min_el]}, максимальный элемент {arr1[max_el]}')

if min_el > max_el:
    min_el, max_el = max_el, min_el # изменение положения макс и мин для корректной работы алгоритма

s = 0
el = [] # для проверки суммируемых данных
for i in range(min_el+1, max_el):
    s += arr1[i]
    el.append(arr1[i])
# print(el)
print(f'Сумма {el} элементов = {s}')



