# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n = int(input("Enter number of elements in massive: "))
x = int(input("Enter searching number: "))
array = [random.randint(1, 10) for i in range(n)]
print(array)
min_set = set()
min = abs(x - array[0])
elem = array[0]
for i in range(n):
    if abs(x - array[i]) < min and array[i] != x:
        min = abs(x - array[i])
        elem = array[i]
min_set.add(elem)
for i in range(n):
    if abs(x - array[i]) == min and array[i] != x:
        min = abs(x - array[i])
        elem = array[i]
        min_set.add(elem)
print(f"Number closest to the number {x} from the given array {min_set}.")
