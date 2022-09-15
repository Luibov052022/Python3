# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import *

my_list = [randint(0, 10) for i in range (randint(5, 10))]
print(my_list)
len = len(my_list)
sum = 0
for i in range (1, len, 2):
    sum += my_list[i]
print(sum)    