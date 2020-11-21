'''     less_6_task_1

Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.

Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
а) выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
б) написать 3 варианта кода (один у вас уже есть);
в) проанализировать 3 варианта и выбрать оптимальный;
г) результаты анализа (количество занятой памяти в вашей среде разработки) вставить в
виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
д) написать общий вывод: какой из трёх вариантов лучше и почему.

Ур. 3, задача 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Самый минимальный и максимальный элементы в сумму не включать.
'''

import sys
import random

def str1(x):
    '''Функция подсчёта байт'''
    # size = sys.getsizeof(x)
    sum_num = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                str1(key)
                str1(value)
        elif not isinstance(x, str):
            # sum_num = 0
            for item in x:
                str1(item)
                sum_num += sys.getsizeof(item)
                # sum_num += item
            # sum_num = sys.getsizeof(sum_num)
            return sum_num
    # Если объект целого типа '__int__'(магический метод), то вычисляем сумму байт
    if hasattr(x, '__int__'):
        sum_num += sys.getsizeof(x)
        return sum_num

# def show(x):
#     size = sys.getsizeof(x)
#     if hasattr(x, '__iter__'):
#         if hasattr(x, 'items'):
#             for key, value in x.items():
#                 size += show(key)
#                 size += show(value)
#         elif not isinstance(x, str):
#             size += sum(map(sizeof, x))
#             # size += str1(x)
#             # for item in x:
#             #     size += item
#         elif isinstance(x, tuple):
#             size += str1(x)
#         elif isinstance(x, set):
#             size += str1(x)
#     size1 += sys.size
#
#     print(f'{type(x)=}, {sys.getrefcount(x)=}, {sys.getsizeof(x)=}, {x=}')
#     print(f'Сумма всех элементов {size=}')
# locals()
    # if isinstance(obj, (list, tuple, set, frozenset)):
    #     size += size1 + sum(map(sizeof, obj))


# SIZE = 10  # Размер массива
SIZE = [63, 86, 44, 41, 80, 48, 56, 39, 43, 20]
MIN_ITEM = 0  # Минимальное значение
MAX_ITEM = 100  # максимальное значение исключительно (99)

# Создание массива вынесено в отдельнуою функцию
def array(n):
    # def array(MIN_ITEM, MAX_ITEM, SIZE)
    # arr1 = [63, 86, 44, 41, 80, 48, 56, 39, 43, 20]
    # arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]  # создание случайных чисел в 1-м массиве с
    arr1 = n
    # show(arr1)
    # get_size(arr1)
    return arr1


def main(n):
    # arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создание случайных чисел в 1-м массиве с
    sums = 0
    arr1 = array(n)
    print(arr1)
    # sums += sys.getsizeof(arr1)
    sums += str1(arr1) # Вызов функции str() для подсчёта байт с нарастающим итогом
    min_el = 0
    max_el = 0
    for i in range(1, len(arr1)):
        if arr1[i] < arr1[min_el]:
            min_el = i
        elif arr1[i] > arr1[max_el]:
            max_el = i
    sums += str1(min_el)
    sums += str1(max_el)
    # sums += sys.getsizeof(min_el)
    # sums += sys.getsizeof(max_el)
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
    sums += str1(el)
    sums += str1(s)
    # sums += sys.getsizeof(el)
    # sums += sys.getsizeof(s)
    n = f'Сумма {el} элементов = {s}'
    print(n)
    print(f'Занимаемый объём памяти: {sums} байт')
    # dir(sums)
    # get_size(n)
    # return n


# num = 10
main(SIZE)
# print(main(num))
# print(get_size(main(num)))
# print(show(main(num)))
# show(30)
'''
[63, 86, 44, 41, 80, 48, 56, 39, 43, 20]
Сумма [44, 41, 80, 48, 56, 39, 43] элементов = 351
Занимаемый объём памяти: 280 байт
'''

