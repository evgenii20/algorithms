'''     lesson_7_task_2

2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

import random

SIZE = 10  # Размер массива
MIN_ITEM = 0  # Минимальное значение
MAX_ITEM = 50  # максимальное значение исключительно


def arr(SIZE):
    '''Генерация случайного списка'''
    arr1 = [round(random.uniform(MIN_ITEM, MAX_ITEM,), 2) for _ in range(SIZE)]
    return arr1


def merge_sort(array):
    '''Алгоритм сортировки слиянием'''
    if len(array) < 2:
        return array

    # если длинна массива = 2-м элементам, то меняем местами
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    # разделяем на 2 части
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    k, j = 0, 0
    # сравниваем левую и правую часть
    while len(left) > k and len(right) > j:
        if left[k] < right[j]:
            array[k + j] = left[k]
            k += 1
        else:
            array[k + j] = right[j]
            j += 1

    while len(left) > k:
        array[k + j] = left[k]
        k += 1
    while len(right) > j:
        array[k + j] = right[j]
        j += 1

    return array


a = arr(SIZE)
print(a)
'''Вызов функции сортировки'''
merge_sort(a)
print(f'Отсортированный массив: \n\t{a}')

