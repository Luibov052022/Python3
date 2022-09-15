# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import *

my_list = [randint(0, 10) for i in range (randint(5, 10))]
print(my_list)
len = len(my_list)
new_list = []
for i in range (int(len/2)):
    new_list.append(my_list[len - i -1] * my_list[i])
print(new_list)    