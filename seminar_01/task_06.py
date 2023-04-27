# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n = input("Enter ticket number with 6 digits: ")
if len(n) == 6:
    x1 = int(n[:3])
    x2 = int(n[3:])
    sum_x1 = 0
    sum_x2 = 0
    while x1 != 0:
        sum_x1 += x1 % 10
        x1 //= 10
    while x2 != 0:
        sum_x2 += x2 % 10
        x2 //= 10
    if sum_x1 == sum_x2:
        print("Lucky ticket!")
    else:
        print("Common ticket")
else:
    print("Wrong number")