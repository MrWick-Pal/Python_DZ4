# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$ 
d = input("Введите число d: ")

if float(d) < (10**-1) and float(d) > (10**-10) or float(d) == (10**-1) or float(d) == (10**-10):
    count_num_after = - 1

    for i in d:
        if i != ".":
            count_num_after += 1
    if count_num_after == 0:
        print(3)
    else:
        result = 4
        iteration = 100000
        count = 0
        d_num = 3

        while count < iteration:
            if count == 0 or count % 2 == 0:
                result = result - (4/d_num)
                d_num += 2
                count += 1
            else:
                result = result + (4/d_num)
                d_num += 2
                count += 1

        result = str(result)
        count = 0
        num_after = 2 + count_num_after
        answer = ''
        for i in result:
            answer += i
            count += 1
            if count == num_after:
                break
        print(answer)
else:
    print("Число d введено неверно!")