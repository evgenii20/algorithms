'''     lesson_7_task_3

3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
'''

import random

M = 4 # Медиана
SIZE = 2 * M + 1  # Размер массива
MIN_ITEM = 0  # Минимальное значение
MAX_ITEM = 50  # максимальное значение исключительно


def arr(SIZE):
    '''Генерация случайного списка'''
    arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return arr1


def median(array):
    # нахождение медианы
    if len(array) % 2 == 1:
        for i in array:
            num = i
            b = 0

            for j in array:
                if i < j:
                    b += 1
            if len(array) == 2 * b + 1:
                return num


a = arr(SIZE)
print(a)
'''Вызов функции сортировки'''
median(a)
print(f'Медиана не отсортированного списка: {median(a)}\n')
print(f'Отсортированный массив: \n\t{sorted(a)}')


