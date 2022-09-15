# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) 

N = int(input("Введите N: "))
my_list = [0]
for i in range(1, N+1):
     my_list.append(fibonacci(i))
my_list.insert(0, 1)
my_list.insert(0, -1)
for j in  range(3, N+1):
    my_list.insert(0, my_list[1]-my_list[0])
print(my_list) 