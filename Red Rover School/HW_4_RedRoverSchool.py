print('''4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата.
------------------------------------------------------------------------------''')
def square(a):
    return (a * 4, a * a, (2*a**2)**(1/2))

print(f'Периметр квадрата: {square(5)[0]}')
print(f'Площадь квадрата: {square(5)[1]}')
print(f'Диагональ квадрата: {round(square(5)[2], 2)}')
print('--------------------------------------------------------------------------')

print('''4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов
и выводит их построчно в формате аргумент: значение. Например:
name: John
last_name: Smith
age: 35 
position: web developer''')
print('--------------------------------------------------------------------------')
def fun_1(**kwargs):
        print(kwargs)
        for key, value in kwargs.items():
            print(f'{key}:{value}')
fun_1(name='Nata', last_name = 'Smolyak', age = 51, position = 'QA Engineer')
print('--------------------------------------------------------------------------')

print(''' 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21]
создайте новый список, содержащий только положительные числа''')
print('--------------------------------------------------------------------------')
my_list = [20, -3, 15, 2, -1, -21]
print('Начальный список:', my_list)
filtred = list(filter(lambda x: x > 0, my_list))
print('Только положительные элементы: ', *filtred)
print('--------------------------------------------------------------------------')

print('''4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке''')
print('--------------------------------------------------------------------------')
from functools import reduce
my_list = [20, -3, 15, 2, -1, -21]
print('Начальный список:', my_list)
result = reduce(lambda x, y:  x*y, my_list)
print(f'Результат перемножения элементов списка: {result}')
print('--------------------------------------------------------------------------')

print('''4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра''')
print('--------------------------------------------------------------------------')
import datetime
def timemometr(func):
    from time import time
    def wrapper(*args):
        start_time = time()
        print(f'Время начала выполнения программы: {start_time}')
        value = func(*args)
        end_time = time()
        print(f'Время окончания работы программы: {end_time}')
        #end_time = datetime.datetime.now()
        execution_time = end_time - start_time
        print(f'Время выполнения программы: {execution_time} сек.')
        return value
    return wrapper

@timemometr
def fact(a):
    # from time import sleep
    # sleep(2)
    res = 1
    for i in range(1, a+1):
        res = res * i
        #print(res)
    return res
fact(100000)
#print(fact(10000))

print('--------------------------------------------------------------------------')
print('''4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
Примените эти функции в качестве методов в другом файле.''')
print('--------------------------------------------------------------------------')

