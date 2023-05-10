# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Enter the 1st element: "))
d = int(input("Enter difference: "))
n = int(input("Enter number of elements: "))

progression = [(a+(i-1)*d) for i in range(1, n+1)]
print(progression)
