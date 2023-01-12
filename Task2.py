#  Даны два файла, в каждом из которых находится запись многочлена. 
#  Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

# with open('eq_1.txt', 'w') as file:
#     file.write('5*x**4 + 4*x**3 + 3*x**2 + 2*x**1 + 1 = 0')

# with open('eq_2.txt', 'w') as file:
#     file.write('1*x**4 + 2*x**3 + 3*x**2 + 4*x**1 + 5 = 0')


def create_list(str):
    str = str.replace(' = 0', '').replace('x', ' ').replace('*', '').replace('**', '').replace(' +', '').split(' ')
    return str

def create_file(str):
    with open('summ_equation.txt', 'w') as data:
        data.write(str)
    print('summ_equation.txt created')

def create_dict(list, dict):
    for i in range(len(list)):
        if i % 2 != 0:
            list += "0"
        if i % 2 == 0:
            dict.update({int(list[i+1]): int(list[i])})
    return dict

def find_summ(dict1, dict2):
    for keys, values in dict1.items():
        for k, v in dict2.items():
            if keys == k:
                summ.update({k: values + v})
    return summ

def summ_eq(equation):
    eq_str = ''
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
    if eq_str.endswith('+ '):
        eq_str = eq_str.rstrip('+ ')
    eq_str += f' = 0'
    return eq_str

with open('eq_1.txt', 'r') as data:
    str1 = data.readline()
with open('eq_2.txt', 'r') as data:
    str2 = data.readline()
print(f"Первый многочлен: {str1}")
print(f"Второй многочлен: {str2}")

list1 = create_list(str1)
list2 = create_list(str2)
#print(list1)
#print(list2)

dict1 = {}
dict2 = {}
print(create_dict(list1, dict1))
print(create_dict(list2, dict2))
print('-'*30)
summ = {}
summ = find_summ(dict1, dict2)
print(summ)
eq_str = summ_eq(summ)
print(eq_str)
create_file(f'{str1}\n + \n{str2}\n = \n{eq_str}')





