# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

#old_list = [213, 43645, 435.5, 'asdasdasd', [2, 35], 82374, 'wqewqe', 82736, 'ufsydg', '!!!!!', 999999,6864, "erjn"]
n = int(input("Задайте длину списка: "))
old_list = []
l = 0
while l < n:
    old_list.insert(l, input("Введите элемент списка: "))
    l += 1
new_list = []
if len(old_list) % 2 == 0:
    for i, j in enumerate(old_list):
        if i % 2 != 0:
            new_list.insert(i - 1, j)
#            print('четное', i, j)
        else:
            new_list.insert(i + 1, j)
#            print('нечетное', i, j)
else:
    for i, j in enumerate(old_list):
        if i < len(old_list):
            if i % 2 != 0:
                new_list.insert(i - 1, j)
#                print('четное', i, j)
            else:
                new_list.insert(i + 1, j)
#                print('нечетное', i, j)
print(old_list)
print(new_list)
old_list = new_list
print(old_list)
print(new_list)