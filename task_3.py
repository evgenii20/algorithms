'''     less_6_task_3

Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.

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


# SIZE = 10  # Размер массива
SIZE = [63, 86, 44, 41, 80, 48, 56, 39, 43, 20]
MIN_ITEM = 0  # Минимальное значение
MAX_ITEM = 100  # максимальное значение исключительно (99)

# Создание массива вынесено в отдельнуою функцию
def array_3(n):
    # def array(MIN_ITEM, MAX_ITEM, SIZE)
    # arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]  # создание случайных чисел в 1-м массиве с
    arr1 = n
    # show(arr1)
    # get_size(arr1)
    return arr1


def main_3(n):
    # arr1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создание случайных чисел в 1-м массиве с
    sums = 0
    arr1 = array_3(n)
    print(array_3(n))
    # sums += sys.getsizeof(arr1)
    sums += str1(arr1) # Вызов функции str() для подсчёта байт с нарастающим итогом
    min_el = 0
    max_el = 0
    # for i in range(1, len(arr1)):
    #     if arr1[i] < arr1[min_el]:
    #         min_el = i
    #     elif arr1[i] > arr1[max_el]:
    #         max_el = i
    i = 0
    while i < len(arr1):
        if arr1[i] < arr1[min_el]:
            min_el = i
        if arr1[i] > arr1[max_el]:
            max_el = i
        i += 1

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
main_3(SIZE)

'''
Версия интерпретатора: 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32,
Операционная система: Windows 64bit'''

'''
1) task_1.py
[63, 86, 44, 41, 80, 48, 56, 39, 43, 20]
Сумма [44, 41, 80, 48, 56, 39, 43] элементов = 351
Занимаемый объём памяти: 280 байт

2) task_2.py
[63, 86, 44, 41, 80, 48, 56, 39, 43, 20]
Сумма [41] элементов = 41
Занимаемый объём памяти: 56 байт

3) task_3.py
[63, 86, 44, 41, 80, 48, 56, 39, 43, 20]
Сумма [44, 41, 80, 48, 56, 39, 43] элементов = 351
Занимаемый объём памяти: 280 байт

Несмотря на то, что 2-й вариант занимает меньше места в памяти при одинаковых условиях из результата видно,
что где-то в коде программист допустил серьёзную ошибку и данный алгоритм нуждается в оптимизации, а 1-й и 3-й
вариант исполнения показывают одинаковый результат при использовании разных циклов внутри кода, поэтому нет разницы 
использования 1-го и 3-го варианта, но если брать в расчёт время исполнения кода с прошлых уроков, то 1-й вариант
с использованием цикла 'for' работает быстрее и предпочтительнее в данном примере.  
'''