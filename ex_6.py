# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с
# параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# Объявление
i = 0
k0 = []
k1 = []
k2 = []
# Заполнение списков
k0.append(input("название: "))
k0.append(input("цена: "))
k0.append(input("количество: "))
k0.append(input("единица: "))

k1.append(input("название: "))
k1.append(input("цена: "))
k1.append(input("количество: "))
k1.append(input("единица: "))

k2.append(input("название: "))
k2.append(input("цена: "))
k2.append(input("количество: "))
k2.append(input("единица: "))

print(k0)
print(k1)
print(k2)

matrix = {tuple(k0), tuple(k1), tuple(k2)}
print(matrix)

d1 = []
d2 = []
d3 = []
d4 = []

dict = {"название": d1, "цена": d2, "количество": d3, "единица": d4}
print(dict)
d1.append(k0[0])
d1.append(k1[0])
d1.append(k2[0])

d2.append(k0[1])
d2.append(k1[1])
d2.append(k2[1])

d3.append(k0[2])
d3.append(k1[2])
d3.append(k2[2])

d4.append(k0[3])
d4.append(k1[3])
d4.append(k2[3])

print(dict)
