# Task18 Python
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите число n:"))
list1 = []
i = 1
for i in range(n):
    list1.append(i+1)
    i += 1
print(list1)
x = 6
print(x)
res = 0
for i in range(len(list1)):
    if list1[0] >= x:
        res = list1[0] - x
    else:
        res = x - list1[0]
    print('Саммый близкий элемент к заданному числу:', res)
    break
