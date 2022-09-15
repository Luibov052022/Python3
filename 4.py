# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input("Введите число: "))
my_list = []
while int(number) != 0:
    mod = int(number % 2)
    number = number / 2
    my_list.append(mod)
my_list.reverse()    
print(*my_list)    
    
