# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, \
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек в длину:'))
m = int(input('Введите количество долек в ширину:'))
k = int(input('сколько долек отломить:'))
if (k%n == 0 or k%m == 0) and (m*n > k):
    print(f'{n} {m} {k} -> yes')
else:
    print(f'{n} {m} {k} -> no')