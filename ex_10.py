# Минимум из трёх чисел
# Условие:
# Напишите программу, которая принимает три числа и выводит наименьшее из них.
#
# Пример ввода:
# Введите первое число: 7
# Введите второе число: 2
# Введите третье число: 5
# Пример вывода:
# Наименьшее число: 2

num1 = int(input())
num2 = int(input())
num3 = int(input())

num_min = min(num1, num2, num3)

print(num_min)