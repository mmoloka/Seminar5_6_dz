# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
#    0,56 -> 11

sum = 0
digits = list(map(lambda i: int(i), list(filter(lambda x: x.isdigit(), input('Введите вещественное число: ')))))
for j in digits:
    sum += j
print(sum)