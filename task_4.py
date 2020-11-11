'''
    less_3_hw_4
Определить, какое число в массиве встречается чаще всего.
'''

import random

SIZE = 10 # Размер массива
MIN_ITEM = 0    # Минимальное значение
MAX_ITEM = 100  # максимальное значение

array1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создание случайных чисел в 1-м массиве с
print(array1)

num = []
max_freq = 1  # встречаемость минимум 1 раз
for i in range(len(array1) - 1):
    freq = 1
    for j in range(i + 1, len(array1)):
        if array1[i] == array1[j]:
            freq += 1   # увеличиваем флаг на 1
    if freq > max_freq:
        max_freq = freq
        num = array1[i]

if max_freq > 1:
    print(f'{max_freq}, раз(а) встречается число {num}')
else:
    print('Все элементы уникальны')

