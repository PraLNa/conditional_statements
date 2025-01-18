# Напишите программу, которая проверяет,
# что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.

number = input()

if len(number) == 4 and number.isdigit():
    first_digit = int(number[0])
    second_digit = int(number[1])
    third_digit = int(number[2])
    fourth_digit = int(number[3])

    if first_digit + fourth_digit == second_digit - third_digit:
        print("ДА")
    else:
        print("НЕТ")
