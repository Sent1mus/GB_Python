# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.


n = int(input("Enter number of elements in 1st array: "))
m = int(input("Enter number of elements in 2nd array: "))
list1 = []
list2 = []
list3 = []

for i in range(n):
    list1.append(int(input("Enter number of 1st list: ")))
for i in range(m):
    list2.append(int(input("Enter number of 2nd list: ")))

for i in range(n):
    if list1[i] not in list3:
        list3.append(list1[i])
for i in range(m):
    if list2[i] not in list3:
        list3.append(list2[i])


def quick_sort(listX):
    if len(listX) <= 1:
        return listX
    temp = listX[0]
    list4 = []
    list5 = []
    for i in range(1, len(listX)):
        if listX[i] < temp:
            list4.append(listX[i])
        else:
            list5.append(listX[i])
    return (quick_sort(list4)+[temp]+quick_sort(list5))


print(list1)
print(list2)
print(quick_sort(list3))
