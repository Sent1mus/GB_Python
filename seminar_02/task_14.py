# Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.

N = int(input("Enter number-limiter:"))
k = 0
print(f"Degree of  {N}: ")
while 2**k < N:
    print(2**k)
    k += 1
