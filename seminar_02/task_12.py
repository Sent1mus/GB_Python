# Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
# а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 3 2

sum = int(input("Enter the sum of two natural numbers: "))
multiply = int(input("Enter the multiplication of these natural numbers: "))
x = int((sum+(sum**2-4*multiply)**0.5)/2)
y = int((sum-(sum**2-4*multiply)**0.5)/2)
print(f"Your riddle numbers are {x} and {y}")
