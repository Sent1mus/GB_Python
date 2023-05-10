#Задача 32: Определить индексы элементов массива (списка), значения которых
#принадлежат заданному диапазону (т.е. не меньше заданного минимума и
#не больше заданного максимума).
#  [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_num = int(input("Enter minimum range: "))
max_num = int(input("Enter maximum range: "))
array_index = []
for i in range(len(array)):
    if min_num <= array[i] <= max_num:
        array_index.append(i)
print(array_index)        