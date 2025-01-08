# Простое калькуляторное меню:
#
# Задача: Выполнить выбранную арифметическую операцию.

print("Выберете операцию: +, -, *, /")
operation = input("Введите операцию: ")
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
if operation == "+":
    print(f"результат сложения: {num1 + num2}")
elif operation == "-":
    print(f"результат вычитания: {num1 - num2}")
elif operation == "*":
    print(f"результат умножения: {num1 * num2}")
elif operation == "/":
    if num2 != 0:
        print(f'результат деления: {num1 / num2}')
    else:
        print('на нуль делить нельзя')
else:
    print('не верная операция')
