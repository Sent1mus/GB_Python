# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input("Enter number of coins: "))
import random
array = [random.randint(0, 1) for i in range(n)]
print(array)
heads = 0
tails = 0
for i in range(n):
    if array[i] == 1:
        heads +=1
    else:
        tails +=1 
if (heads<tails):
    print(f"Need to flip {heads} coin")
else:
    print(f"Need to flip {tails} coin")