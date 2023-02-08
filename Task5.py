# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

first_poly = []
second_poly = []

with open('file1.txt') as f:
    first_poly = list(map(str, f.read().split()))

with open('file2.txt') as f:
    second_poly = list(map(str, f.read().split()))

poly_sum = [] 

for i in first_poly:
    if i == str(0):
        first_poly.remove(i)
   
for i in first_poly:
    if i == '=':
        first_poly.remove(i)
    else:
        poly_sum.append(i)

for i in second_poly:
    if i == str(0):
        second_poly.remove(i)

for i in second_poly:
    if i == '=':
        second_poly.remove(i)
    else:
        poly_sum.append(i)

file = open("file3(result).txt", "w")
file.write("Sum: ")
file.write(''.join(map(str,first_poly)))
file.write(" + ")
file.write(''.join(map(str,second_poly)))
file.write(" = ")
file.write("0 ")
file.close()