# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
print('----------------Задание 3.1-------------')
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])

print('-----------Option 1--------')
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

print('--------------Option 2. Using deconstruction----------')
my_list = ['a', 'b', [1, 2, 3], 'd']
list1 = my_list[2]
print(*list1, sep='\n')


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

print('----------------Задание 3.2-------------')
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
s = 0
for i in list_1:
    if type(i) == int:
        s = s + i
print(f'Сумма чисел списка = {s}')
print()
print("--------Строки с буквой 'a'----------")
for i in list_1:
    if 'a' in str(i):
        print(i)

print('----------------Задание 3.2- Решение от ментора------------')
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#a) Using filter get sum of all integers
print(sum(filter(lambda x: isinstance(x, int), list_1)))
#b) Using list comprehension print string which contain 'a'
print([x for x in list_1 if isinstance(x, str) and 'a' in x])


#3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
print('-------Превращение листа в кортеж------------')
lst = ['cat', 'dog', 'horse', 'cow']
print(f'Это список: {lst} {type(lst)}')
my_tuple = tuple(lst)
print(f'Это кортеж: {my_tuple} {type(my_tuple)}')


# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
print('---------------Каякая семья больше--------------')
family_1 = input('Введите членов семьи 1 через запятую: ')
family_2 = input('Введите членов семьи 2 через запятую: ')
print('Семья 1: ', family_1)
print('Семья 2: ', family_2)
family_1 = family_1.split(',')
family_2 = family_2.split(',')
if len(family_1) > len(family_2):
    print(f'Семья с бОльшим составом:  {family_1}, в ней {len(family_1)} человек')
elif len(family_2) > len(family_1):
    print(f'Семья с бОльшим составом:  {family_2}, в ней {len(family_2)} человек')
else:
    print('Состав семей одинаков')

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

print('-------------------Мой словарь--------------')
film = {
    'title': 'Бриллиантвая рука',
    'director': 'Леонид Гайдай',
    'year': 1968,
    'budget': '450 000 рублей',
    'main_actor': 'Юрий Никулин',
    'slogan': 'Федя - дичь!'
}
print(film)
print('-------------------Вывод ключей в виде списка--------------')

keys = list(film.keys())
print(keys)

print('-------------------Вывод значений- в виде списка-------------')
values = list(film.values())
print(values)

print('-------------------Вывод ключей и значений-в виде списка-------------')
items = list(film.items())
print(items)
print()
#3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print('-------------------Сумма всех значений в словаре------------')
my_dictionary = {'num1': 'dddg', 'num2': 567, 'num3': -37, 'num4': 21}
values = list(my_dictionary.values())
s = 0
for i in values:
    if type(i) == int:
        s = s + i
print(f'Сумма всех значений в словаре: {s}')
print()

#3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
print('-------------------Удаление повторяющиеся значения из списка------------')
lst = [1, 2, 3, 4, 5, 3, 2, 1]
print('Первоначальный список: ', lst)
st = set(lst)
print('Преобразуем список в множество: ', st)
print('Окончательный список: ', list(st))
print()

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
print('----------Операции с множествами------------------')
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print('Пересечение множеств: ', set1.intersection(set2))
print('Значения, отсутствующие в обоих множествах: ', set1.symmetric_difference(set2))
print('Является ли set1 подмножеством set2: ', set1.issubset(set2))
print('Является ли set2 подмножеством set1: ', set2.issubset(set1))
