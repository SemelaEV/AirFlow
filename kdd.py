# lists = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# for m_list in lists:
#     for element in m_list:
#         print(element, end=" ")
#     print(" ")
#
#
# m_list = ["apple", "banana", "cherry"]
#
# for index, item in enumerate(m_list):
#     print(index, item)

# m_list = [i for i in range(100)]
# print(m_list)

# m_list_1 = []
# for i in range(100):
#     m_list_1.append(i)
# print(m_list_1)

# m_list = [2,5,6,8,4,4,8,1,7,25]
# m_list.sort()
# print(m_list)
# m_list_1 = ["apple", "Banana", "Kiwi", "cherry"]
# m_list_1.sort(key=str.lower)
# print(m_list_1)


# m_list = [1,1,2,2]
# m_list_1 = []
# for i in m_list:
#     if i not in m_list_1:
#         m_list_1.append(i)
# print(len(m_list_1), m_list_1)

# empty_set = set()
# print(empty_set)

# Напишите программу, которая считает количество знаков пунктуации в символьной строке.
# К знакам пунктуации относятся символы из набора ".,;:!?".
# Набор должен храниться в виде множества.
# Пример:
# Введите строку: Я! Есть. Грут?! Я, Грут и Есть.
# Количество знаков пунктуации: 6

# user = input()
# my_set = set(".,;:!?")
# a = 0
# for i in user:
#     if i in my_set:
#         a += 1
# print(a)

# Напишите программу, которая находит все различные цифры в символьной строке.
# Для решения используйте множество (цифры будут различные, и поиск во множестве
# намного быстрее, чем в списке).
# Подсказка: можно использовать вот такое сравнение '0'<=x<='9'
# Пример:
# Введите строку: ab1n32kz2
# Различные цифры строки: 123

# ПЕРВАЯ РЕШЕННАЯ ЗАДАЧА НА ЛЕКЦИИ
# my_set = set(input("Введите строку: "))
# my_set_1 = set()
# for element in my_set:
#     if '0' <= element <= '9':
#         my_set_1.add(element)
# print("Различные цифры строки: ", *my_set_1)

# user = {
#     "name": "Alex",
#     "age": "26",
#     "city": "Moscow"
# }


# def func(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
#
# func(name="Alex", age=26, city="Moscow")

# string = []
# count = 0
# while count < 5:
#     string.append(input())
#     count += 1
# print(string)

# N друзей постоянно берут в долг друг у друга деньги. В какой-то момент им надоело забывать, кто, кому и сколько должен, и они придумали систему долговых расписок. Чтобы начать новый год «с чистого листа», друзья решили оплатить все долговые расписки, которые у них накопились друг к другу. Однако выяснилось, что иногда один и тот же человек в разные дни выступал как в роли должника, так и в роли кредитора.
# Напишите программу, которая по заданным распискам вычислит, сколько всего каждый должен выплатить другим (или получить с других).
# Сначала вводится число N — количество друзей, затем вводится число K — количество долговых расписок, после этого следует K троек чисел: номер друга, взявшего в долг; номер друга, давшего деньги; и сумма. Гарантируется, что ни один друг не брал в долг сам у себя.
# Программа должна вывести «баланс друзей», то есть суммы, которые должны получить или отдать друзья. Положительное число означает, что друг должен получить деньги от других, отрицательное — должен отдать деньги.
# Пример 1:
# Кол-во друзей: 2
# Долговых расписок: 3
# 1-я расписка
# Кому: 1
# От кого: 2
# Сколько: 10
# 2-я расписка
# Кому: 1
# От кого: 2
# Сколько: 20
# 3-я расписка
# Кому: 1
# От кого: 2
# Сколько: 20
# Баланс друзей:
# 1: -50
# 2: 50


# n = int(input('Введите кол-во друзей: '))
# k = int(input('Введите кол-во долговых расписок: '))
# papers = []
#
# for i in range(k):
#     papers.append(tuple(input("Введите номера друзей, сумму: ").split()))
#
# cash = [0 for friend in range(n)]
#
# for paper in papers:
#     cash[int(paper[0]) - 1] += int(paper[2])
#     cash[int(paper[1]) - 1] -= int(paper[2])
#
# print(cash)

# print(papers)

# a = int(input())
#
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
#
# p = (a + b) * (a + b)
# print(p)

# m_dict = {
#     "key": "value"
# }
# m_dict_1 = m_dict.copy()
# m_dict["key"] = "value1"
# print(m_dict_1)

# В базе данных магазина вся необходимая информация по товарам делится на два словаря:
# первый отвечает за коды товаров, второй — за списки количества разнообразных товаров
# на складе:
# goods = {
#  'Лампа': '12345',
#  'Стол': '23456',
#  'Диван': '34567',
#  'Стул': '45678',
# }
# store = {
#  '12345': [
#  {'quantity': 27, 'price': 42},
# ],
#  '23456': [
#  {'quantity': 22, 'price': 510},
#  {'quantity': 32, 'price': 520},
#  ],
#  '34567': [
#  {'quantity': 2, 'price': 1200},
#  {'quantity': 1, 'price': 1150},
#  ],
#  '45678': [
#  {'quantity': 50, 'price': 100},
#  {'quantity': 12, 'price': 95},
#  {'quantity': 43, 'price': 97},
#  ],
# }
#
# Каждая запись второго словаря отображает, сколько и по какой цене закупалось
# товаров (цена указана за 1 шт.).
# Напишите программу, которая рассчитывает, на какую сумму лежит каждого
# товара на складе, и выводит эту информацию на экран.
# б

# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
# store = {
#     '12345': [{'quantity': 27, 'price': 42},],
#     '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520},],
#     '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150},],
#     '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97},],
# }
#
# warehouse = {}
#
# for key, value in store.items():
#     summa = 0
#     for element in value:
#         summa += element['quantity'] * element['price']
#
#     warehouse[key] = summa
# print(warehouse)
#
# for key, value in goods.items():
#     print((f'Товар {key} закуплен на общую сумму: {warehouse[value]}'))

# person = {"name": "Alice", "age": 25, "city": "New York"}
# value_to_find = 25
#
# # Используем генератор для проверки наличия значения
# if any(value == value_to_find for value in person.values()):
#     print(f"Значение {value_to_find} присутствует в словаре.")
# else:
#     print(f"Значение {value_to_find} отсутствует в словаре.")



# dict_one = {"one": "eon", "two": "two", "four": True}
# dict_two = {"two": "own", "zero": 4, "four": True}
# def gen_diff(d_one, d_two):
#     result = {}
#     for key, value in d_one.items():
#         if key in d_two:
#             if d_one[key] == d_two[key]:
#                 result[key] = f'unchanged {value}'
#             else:
#                 result[key] = f'changed {value} to value {d_two[key]}'
#         else:
#             result[key] = f'deleted {value}'
#     for key, value in d_two.items():
#         if key not in result:
#             result[key] = f'added {value}'
#
#
#     print(result)
#     return result
#
#
# gen_diff(dict_one, dict_two)

