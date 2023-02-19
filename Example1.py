# Задача 1: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input('Введите трехзначное число: ')
result = 0
for i in number:
    result = result + int(i)
print(f"{number} -> {result}") 