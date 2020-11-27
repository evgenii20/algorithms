'''     Lesson_8_task_1

1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции
дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
'''


import hashlib


def search_sub(s):
    len_s = len(s) # Определяем длинну строки
    info_sub = []   # для наглядности
    # объявим множество для хранения подстрок хешей
    # не индексированное, изменяемое, хранит уникальные элементы
    set_hash_sub = set()

    '''Перебор строки '''
    # сдвигаем длину строки на 1
    for i in range(len_s + 1):
        # сдвигаем начальный индекс подстроки в позицию i + 1
        for j in range(i + 1, len_s + 1):
            # проверим на пустоту и равенство исходной строке
            if s[i:j] != '' and s[i:j] != s:
            # if s[i:j + 1] != '' and s[i:j + 1] != s:
                # continue
                h_index = hashlib.sha256(s[i:j].encode('utf-8')).hexdigest()
                set_hash_sub.add(h_index)
                info_sub.append(s[i:j])
                # if s[i:j + 1] == s:
                #     return i
    return f'Количество подстрок: {len(set_hash_sub)}\nСформированные подстроки:\n\t{info_sub}'

# SEARCH = 'abcd' # a, b, c, d, ab, bc, cd, abc, bcd, abcd
STRING = 'abcd'
print(search_sub(STRING)) #, SEARCH))

'''
Для справки:
Количество подстрок: 9
Сформированные подстроки:
	['a', 'ab', 'abc', 'b', 'bc', 'bcd', 'c', 'cd', 'd'] 
'''