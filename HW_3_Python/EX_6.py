# 6. Сравнить 2 строки без учёта регистра
print('Сравнить 2 строки без учёта регистра. Метод LOWER (нижний регистр)')
a = 'Nata'
b = 'nAta'
if a.lower() == b.lower():
    print('TRUE')
else:
    print('FALSE')

print('Сравнить 2 строки без учёта регистра. Метод CASEFOLD (удаляет все различия регистра, присутствующие в строке)')
a = 'Nata'
b = 'nAta'
if a.casefold() == b.casefold():
    print('TRUE')
else:
    print('FALSE')

print('Сравнить 2 строки без учёта регистра. Без IF')
a = 'Nata'
b = 'nAta'
print(a.lower() == b.lower())