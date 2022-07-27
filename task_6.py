# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list1 = [2, 3, 5, 9, 3]
sum = 0
for i in [list1[j] for j in range(len(list1)) if j % 2 != 0]:
    sum += i
print(sum)