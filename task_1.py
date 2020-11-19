'''     lesson_5_hw_1(task_1.py)

Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год
для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего
и ниже среднего.
'''

from collections import namedtuple

# Объявляем класс
Corp = namedtuple('Corp', 'name, q1, q2, q3, q4, years')
# company = Corp('Corp', q1, q2, q3, q4')
# company = Corp('Corp', 0)

# Объявим список для добавления компаний
company = []
CHK = 4
'''Ввод данных о количестве предприятий и их наименований'''
# def in_corp():
p = int(input('Введите количество предприятий: '))
i = 1
pr = 1
years_profit = 0
while i <= p:
    # if pr <= p:
    name = str(input(f'Введите название {i}-го предприятия и нажмите "Enter": '))
    count = 1
    sums = 0
    quarter = [] # Объявим дополнительный список для хранения квартала
    # j = 1
    '''Ввод прибыли предприятий за 4-е квартала'''
    # можно использовать цикл for
    while count <= CHK:
        profit = int(input(f'Введите прибыль {i}-го за {count} квартал и нажмите "Enter": '))
        # profit_q2 = int(input(f'Введите прибыль за 2 квартал и нажмите "Enter": '))
        # profit_q3 = int(input(f'Введите прибыль за 3 квартал и нажмите "Enter": '))
        # profit_q4 = int(input(f'Введите прибыль за 4 квартал и нажмите "Enter": '))
        quarter.append(profit) # сохраняем ввод прибыли за кадый квартал
        # chk -= 1
        sums += profit
        count += 1
    i += 1
    pr += 1
    # comp = company._replace(corp=name, quarter=sums)
    # company = namedtuple('name', Corp._fields + ('sums',))
    # company.append(Corp(name, *quarter, sum(quarter)))
    company.append(Corp(name, *quarter, sums))
    years_profit += sums # profit # сохраним для подсчёта среднего

'''Определение средней прибыли за год для всех предприятий'''
# вычислим среднюю прибыль 'n'-х компаний
average = years_profit / p

print(f'\nСредняя прибыль = {average}')

'''Вывести наименование предприятий чья прибыль выше среднего и ниже среднего'''
print(f'\nПредприятя с прибылью больше среднего:')
for Corp in company:
    if Corp.years > average:
        print(f'Компания {Corp.name} заработала {Corp.years}')
        # print(Corp.quarter[0])   # так можно получить доступ к нужной четверти.

print(f'\nПредприятя с прибылью меньше среднего:')
for Corp in company:
    if Corp.years < average:
        print(f'Компания {Corp.name} заработала {Corp.years}')

# print(company)
