# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 
# или x² + 5 = 0 или 10*x² = 0

import random

def CreateFile(st):
    with open('file.txt', 'w') as data:
        data.write(st)
    print('file.txt created')

def CreateEq(k):
    eq_str = ''
    if k < 1:
        eq_str = 'x = 0'
    else:
        for k,v in equation.items():
            if k == 1:
                if v == 0:
                    eq_str += f''
                elif v == 1:
                    eq_str += f'x + '
                else:
                    eq_str += f'{v}*x + '
            elif k == 0:
                if v == 0:
                    eq_str += f''
                else:
                    eq_str += f'{v} + '
            else:
                if v == 0:
                    eq_str += f''
                elif v == 1:
                    eq_str += f'x**{k} + '
                else:
                    eq_str += f'{v}*x**{k} + '
        else:
            if v == 0:
                eq_str += f''
            else:
                eq_str = eq_str[:-3]
        if eq_str.endswith('+ '):
            eq_str = eq_str.rstrip(' + ')
        eq_str += f' = 0'
    return eq_str

k = int(input('Введите максимальную степень: '))
equation = {}
for i in range(k, -1, -1):
    equation[i] = random.randint(0,100)
 
#print(equation)

print(CreateEq(k))

CreateFile(CreateEq(k))