#Part_1

#1) Создать переменную типа String
item_1 = 'Nata'

#2) Создать переменную типа Integer
item_2 = 51

#3) Создать переменную типа Float
item_3 = 100.562

#4) Создать переменную типа Bytes
item_4 = b' \f\a'

#5) Создать переменную типа List
item_5 = ['Nata', 51, 123.55, 'Hello', [1, 2, 3], True]

#6) Создать переменную типа Tuple
item_6 = (1, 2, 'Nata', True, [7, 8, 9])

#7) Создать переменную типа Set (множество, вывод в произвольном порядке)
item_7 = {'Nata', 51, 123.7, ('Hello', 'World')}

#8. Создать переменную типа Frozen set
item_8 = frozenset({'Nata', 51, 123.7, ('Hello', 'World')})

#9) Создать переменную типа Dict
item_9 = {'name': "Nata",
          'age': 51,
          'location': "RB"}

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(item_1, '-', type(item_1))
print(item_2, '-', type(item_2))
print(item_3, '-', type(item_3))
print(item_4, '-', type(item_4))
print(item_5, '-', type(item_5))
print(item_6, '-', type(item_6))
print(item_7, '-', type(item_7))
print(item_8, '-', type(item_8))
print(item_9, '-', type(item_9))

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
first_name = 'Nata'
last_name = 'Smolyak'
full_name = first_name+' '+last_name
print(full_name)

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
name = 'Nata'
age = 51
print(name, ',', age)
#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
name = 'Nata'
age = 51
print(name+' '+str(age))