# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N
num = int(input('Введите число: '))
list_1 = list()
i = 2

while i <= num:
    if num % i == 0:
        list_1.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(list_1)