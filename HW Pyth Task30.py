# Task30 Python
#Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input("Введите первый элемент a1: "))
d = int(input("Введите раность d: "))
n = int(input("Введите количество элементов n: "))
res = []
for i in range(n):
    an = a1 + (n-1) * d
    res.insert(0, an)
    n -= 1
print(*res)