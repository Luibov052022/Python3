# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import *

my_list = [float(input('Введите число: ')) for i in range (int(input("Сколько чисел? ")))]
print(my_list)
len = len(my_list)
new_list = []
for i in my_list:
    new_list.append(round(i - int(i),2))
print(round(max(new_list) - min(new_list), 2))