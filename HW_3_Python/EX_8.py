# 8. Напишите функцию, которая принимает строку и возвращает количество букв английского алфавита,
# которые встречаются больше чем 1 раз.
def count_eng(s):
    ascii = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    count = 0
    for i in ascii:
        count = 0
        for j in s:
            c = j.casefold()
            if c == i:
                count +=1
        if count > 1:
            print('Буква', i, 'встречается', count, 'раза')
str = input('Введите строку: ')
count_eng(str)

