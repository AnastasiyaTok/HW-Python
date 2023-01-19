# Task8 Python
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input ("Input n: "))
m = int(input ("Input m: "))
k = int(input ("Input k: "))
if ((k%n)==0):
    if (k//n<m):
         print ("yes")
    else:
        print ("no")
elif ((k%m)==0):
    if (k//m<n):
         print ("yes")
    else:
        print ("no")
else:
    print("no")

