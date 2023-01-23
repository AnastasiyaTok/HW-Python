# Task10 Python
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

import random as rn
n = rn.randint(2,10)
table=[]
for i in range (0,n,1):
    table.append(rn.randint(0,1))
zero = 0
for i in range (0,n,1):
    print(table[i])
for i in range (0,n,1):
    if table[i] == 0:
        zero=zero+1
print('Длина массива:', n )
print(zero,"\n ")
if zero == len(table)//2:
    print ("Поровну -  переверните 19 ", zero)
elif (zero < len(table)//2):
    print ("Нужно перевернуть: ", zero)
else:
    print ("Нужно перевернуть: ", len(table)-zero)