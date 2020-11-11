'''
    less_3_hw_5
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию
в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
'''

import random

SIZE = 10 # Размер массива
MIN_ITEM = -50    # Минимальное значение может быть отрицательным '- 100'
MAX_ITEM = 100  # максимальное значение
EL = 50    # отрицательные числа от 0 до 50

array1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]  # создание случайных чисел в 1-м массиве с
print(array1)

num = []
negative = -1  # отрицательное число
for i in range(len(array1)):
    if array1[i] < 0 and negative == -1:
        negative = i
    elif array1[i] < 0 and (array1[i] > array1[negative]):
        negative = i
        i += 1

print(f'Максимальный отрицательный элемент в позиции {negative}: {array1[negative]}')

