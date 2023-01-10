#  Даны два файла, в каждом из которых находится запись многочлена. 
#  Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

with open('eq_1.txt', 'w') as file:
    file.write('5*x**5 + 4*x**4 + 3*x**3 + 2*x**2 + x = 0')

with open('eq_2.txt', 'w') as file:
    file.write('x**4 + 2*x**3 + 3*x**2 + 4*x + 5 = 0')

file1 = 'eq_1.txt'
file2 = 'eq_2.txt'

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

def convert_pol(pol):  # удалили "хвостик" и порезали" строку на массив , разделитель знак " + "
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = {i: pol[i] for i in range(len(pol))}
    # for i in range(len(pol)):
    #     if pol[i] == 'x':
    #         pol[i] = '1'
    #pol = pol[::-1]
    return pol

dict1 = {}
dict2 = {}
pol1 = read_pol(file1)
pol2 = read_pol(file2)
print('Исходные многочлены:')
print(pol1)
print(pol2)
print('_'*30)
print(convert_pol(pol1))
print(convert_pol(pol2))
# pol1_coef = list(map(int, convert_pol(pol1)))
# pol2_coef = list(map(int, convert_pol(pol2)))
# print(pol1_coef)
# print(pol2_coef)
# print('_'*30)






# with open('task034.txt', 'w') as file_sum:
#     file_sum.writelines(sum_pol)