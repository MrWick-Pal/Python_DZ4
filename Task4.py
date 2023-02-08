# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в 
# файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

def write_file(st):
    with open('file1.txt', 'w') as data:
        data.write(st)

k = int(input('Введите натуральную степень k:'))

koeff = [randint(0,100) for i in range(k)] + [randint(1,100)]
answer = ' + '.join([f'{(j, "")[j==1]}x^{i}' for i, j in enumerate(koeff) if j] [::-1])
answer = answer.replace('x^1+', 'x+')
answer = answer.replace('x^0', '')
answer+= ('','1') [answer[-1]=='+']
answer = (answer, answer[:-2]) [answer[-2:]=='^1']

print(answer)
write_file(answer)