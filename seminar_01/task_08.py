#  Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Enter choco length "))
m = int(input("Enter choco width "))
k = int(input("How much pieces you want to eat? "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("You can eat that ")
else:
    print("Sorry, you cant eat that much")