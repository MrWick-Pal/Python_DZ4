# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
list_1 = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {list_1}")

new_list = list()
for i in list_1:
    if i not in new_list:
        new_list.append(i)
print(new_list)