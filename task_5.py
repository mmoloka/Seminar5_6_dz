# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

list1 = ['hello', '12', 'red', '657']
num = 657
if list(filter(lambda i: i == str(num), list1)) == []:
    print('no')
else:
    print('yes')