import sys
# # Задание 2.1
# # Напишите программу, которая проверяет здоровье персонажа в игре.
# # Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
# print('-------------Task 2.1---------------')
# health = int(input("Enter the player's health: "))
# if health >= 0:
#     print('True')
# else:
#     print('False')
#
# # Задание 2.2
# # Напишите программу, которая проверяет является ли введенное число четным.
# # Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
# print('-------------Task 2.2---------------')
# num = int(input("Enter an integer: "))
# if num%2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')
#
# # Задание 2.3
# # Напишите программу, которая проверяет является ли год високосным.
# # Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# # Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
# print('-------------Task 2.3---------------')
# year = int(input('Enter the year: '))
# if year%4 == 0 and year%100 != 0 or year %400 == 0:
#     print("Високосный")
# else:
#     print('Не високосный')
#
# # Задание 2.4
# # Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# # Текст и количество повторений нужно ввести с помощью input()
# print('-------------Task 2.4---------------')
# text = input("Enter text: ")
# num = int(input('Enter the number of iterations: '))
# for i in range(1, num+1):
#     print(text)

# Задание 2.5.
# Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str),
# производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}

print('-------------Task 2.5---------------')
try:
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
except ValueError as e:
    print(f'Введенное занчение не является числом: {e}')
    sys.exit()
operator = input('Operator: ')
if operator not in ("/", '*', '+', '-', '%', '//', '**'):
    print('Некорректный оператор')
    sys.exit()
result = 0
if num2 == 0 and operator == '/':
    try:
        result = num1/num2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    sys.exit()
elif operator == '*':
    result = num1 * num2
elif operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '%':
    result = num1 % num2
elif operator == '//':
    result = num1 // num2
elif operator == '**':
    result = num1 ** num2
else:
    result = num1 / num2
print(f'{num1} {operator} {num2} = {result}')

# EVAL используется для синтаксического анализа строки выражения
#
print('-------------Task 2.5-C использованием функции EVAL--------------')
try:
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
except ValueError as e:
    print(f'Введенное занчение не является числом: {e}')
    sys.exit()
operator = input('Operator: ')
if operator not in ("/", '*', '+', '-', '%', '//', '**'):
    print('Некорректный оператор')
    sys.exit()
result = 0
if num2 == 0 and operator == '/':
    try:
        result = num1/num2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    sys.exit()
else:
    result = eval(f'{num1} {operator} {num2}')
    print(f'{num1} {operator} {num2} = {result}')