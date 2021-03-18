import numpy as np
import math

xi = [0.000, 0.750, 1.500, 2.250, 3.000]
yi = [-1.000, -2.282, -4.358, -7.656, -12.831]

#Вывести на экран x и y
print()
print('xi = ', xi)
print('yi = ', yi)

system = ''
kvadr_yravn = ''
system_2 = ''
polinom = ''

E2 = []
yi_minus_E2 = []

#Вычисляем коэфициенты для первой сис-мы (нахождение z1, z2)
first = round((yi[0]**2) + (yi[1]**2) + (yi[2]**3), 3)
second = round((yi[0] * yi[1]) + (yi[1] * yi[2]) + (yi[2] * yi[3]), 3)
third = round((yi[1]**2) + (yi[2]**2) + (yi[3]**2), 3)
fourth = round(-((yi[0] * yi[2]) + (yi[1] * yi[3]) + (yi[2] * yi[4])), 3)
fifth = round(-((yi[1] * yi[2]) + (yi[2] * yi[3]) + (yi[3] * yi[4])), 3)

#Составление сис-мы
print()
print('Система двух алгебраических уравнений с двумя неизвестными z1, z2: ', end='')
system += ' {' + f'{first} * z1 + {second} * z2 = {fourth}\n'
system += ' {' + f'{second} * z1 + {third} * z2 = {fifth}\n'

#Вывод на экран сис-мы
print()
print(system)

#Вычисление z1, z2
matrix_A = np.array([[first, second], [second, third]])
matrix_B = np.array([fourth, fifth])
answer = np.linalg.solve(matrix_A, matrix_B)

#Вывод полученных z1, z2
print(f'z1 = {round(answer[0], 3)}', f'\nz2 = {round(answer[1], 3)}')

#Составление квадратного уравнения с z1, z2
kvadr_yravn += f'x^2 + ({round(answer[1], 3)}) * x + ({round(answer[0], 3)}) = 0'

#Вывод на экран квадратного уравнения с z1, z2
print()
print('Квадратное уравнение с найденными коэфициентами z1, z2: ', end='')
print()
print(kvadr_yravn)
print()

#Решение квадратного уравнения для получения x1, x2
a = float(1)
b = float(round(answer[1], 3))
c = float(round(answer[0], 3))
 
discr = b**2 - 4 * a * c

if discr > 0:
        x1 = round((-b + math.sqrt(discr)) / (2 * a), 5)
        x2 = round((-b - math.sqrt(discr)) / (2 * a), 5)
        print(f"x1 = {x1}\nx2 = {x2}")
elif discr == 0:
        x = -b / (2 * a)
        print(f"x = {x}")
else:
        print("Корней нет")

#Вычисление lambda1, lambda2
lambda_1 = round(math.log(abs(x1)), 3)
lambda_2 = round(math.log(abs(x2)), 3)

#Вывод на экран lambda1, lambda2
print()
print('lambda1 = ', lambda_1, '\nlambda2 = ', lambda_2)

#Вычисление коэфициентов для второй сис-мы (для нахождения c1, c2)
first_2 = round(1 + (x1**2) + (x1**4), 3)
second_2 = round(1 + (x2**2) + (x2**4), 3)
third_2 = round(1 + (x1*x2) + ((x1**2)*(x2**2)), 3)
fourth_2 = round(yi[0] + (yi[1]*x1) + (yi[2]*(x1**2)), 3)
fifth_2 = round(yi[0] + (yi[1]*x2) + (yi[2]*(x2**2)), 3)

#Составление сис-мы
system_2 += ' {' + f'{first_2} * c1 + {third_2} * c2 = {fourth_2}\n'
system_2 += ' {' + f'{third_2} * c1 + {second_2} * c2 = {fifth_2}\n'

#Вывод сис-мы
print()
print("Система нормальных уравнений с симметричной матрицей: ")
print(system_2)

#Вычисление c1, c2
matrix_C = np.array([[first_2, third_2], [third_2, second_2]])
matrix_D = np.array([fourth_2, fifth_2])
answer_2 = np.linalg.solve(matrix_C, matrix_D)

#Вывод c1, c2 на экран
print(f'c1 = {round(answer_2[0], 3)}', f'\nc2 = {round(answer_2[1], 3)}')

#Составление полинома
polinom += f'E2(t) = {round(answer_2[0], 3)} * e^({lambda_1}*t) - {round(answer_2[1], 3)} * e^({lambda_2}*t)'

#Вывод полинома
print()
print("Аппроксимирующий квазимногочлен: ")
print(polinom)

#Вычисление значения полинома в точке t(от 0 до 4)
for i in range(0, 5):
	E2.append(round(round(answer_2[0], 3) * math.exp(lambda_1*i) - round(answer_2[1], 3) * math.exp(lambda_2*i), 3))

#Вычисление значения (yi - E2) в точке t(от 0 до 4)
for i in range(0, 5):
	yi_minus_E2.append(round(yi[i] - E2[i], 3))

#Вычисление значения (yi - E2)^2 в точке t(от 0 до 4)
yi_minus_E2_kvadr = [round(value**2, 3) for value in yi_minus_E2]

#Вывод таблицы для нахождения Eps
print()
print("Оценим результат: ")
print('----------------------------------------------------------------------------------')
print('tk', '\t\t', 'yk', '\t\t', 'E2(tk)', '\t', 'yk - E2(tk)', '\t', '(yk - E2(tk))^2')
print('----------------------------------------------------------------------------------')

for i in range(0, 5):
	if(i == 0):
		print(i, '\t\t', yi[i], '\t\t', E2[i], '\t', yi_minus_E2[i], '\t\t\t', yi_minus_E2_kvadr[i])
	elif(i == 1):
		print(i, '\t\t', yi[i], '\t', E2[i], '\t', yi_minus_E2[i], '\t\t\t', yi_minus_E2_kvadr[i])
	elif(i == 3):
		print(i, '\t\t', yi[i], '\t', E2[i], '\t\t', yi_minus_E2[i], '\t\t', yi_minus_E2_kvadr[i])
	elif(i == 4):
		print(i, '\t\t', yi[i], '\t', E2[i], '\t', yi_minus_E2[i], '\t\t\t', yi_minus_E2_kvadr[i])
	else:
		print(i, '\t\t', yi[i], '\t', E2[i], '\t', yi_minus_E2[i], '\t\t', yi_minus_E2_kvadr[i])

print('----------------------------------------------------------------------------------')

#Вывод на экран значения Eps
print()
print('Eps^2 = ', round(sum(yi_minus_E2_kvadr), 3))