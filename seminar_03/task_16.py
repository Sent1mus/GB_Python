# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

import random
n = int(input("Enter number of elements in massive: "))
x = int(input("Enter searching number: "))
array = [random.randint(x-10, x+10) for i in range(n)]
print(array)
sum = 0
for i in range(n):
    if array[i] == x:
        sum += 1
print(f"Number {x} occurs in array {sum} times")