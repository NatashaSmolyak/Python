# 3. Все чётные числа вывести в другой список
l = [1, 3, 4, 5, 8, 9, 10, 44, 22, 50, 79, 54, 28, 91]
b = []
for i in l:
    if i%2 == 0:
        b.append(i)
print(b)


