import numpy as np

xi = [0.25, 0.65, 1.05, 1.45, 1.85, 2.25, 2.65, 3.05, 3.45, 3.85]
yi = [1.78, 3.77, 5.68, 7.45, 9.04, 10.40, 11.48, 12.25, 12.64, 12.62]

x_0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#Вывести на экран x и y
print()
print('xi = ', xi)
print('yi = ', yi)

#Вычисление значений списка xi в разных степенях
xi_2 = [round(value**2, 5) for value in xi]
xi_3 = [round(value**3, 5) for value in xi]
xi_4 = [round(value**4, 5) for value in xi]
xi_5 = [round(value**5, 5) for value in xi]
xi_6 = [round(value**6, 5) for value in xi]

yi_xi = []
yi_xi_2 = []
yi_xi_3 = []

system = ''

#Добавление значений yi*xi, yi*xi^2, yi*xi^3 в соответствующие списки
print()
for i in range(0, len(xi)):
	yi_xi.append(round(xi[i] * yi[i], 2))

for i in range(0, len(xi)):
	yi_xi_2.append(round(xi_2[i] * yi[i], 2))

for i in range(0, len(xi)):
	yi_xi_3.append(round(xi_3[i] * yi[i], 2))

#Вывод таблицы со значениями
print()
print('-----------------------------------------------------------------------------------------------------------------------------------')
print('xi', '\t', 'xi**2', '\t\t', 'xi**3', '\t\t', 'xi**4', '\t\t', 'xi**5', '\t\t', 'xi**6', '\t\t', 'yi', '\t', 'yi*xi', '\t ', 'yi*(xi**2)', '\t', 'yi*(xi**3)')
print('-----------------------------------------------------------------------------------------------------------------------------------')

for i in range(0, len(xi)):
	if(i != 7 and i != 8 and i != 9):
		print(xi[i], '\t', xi_2[i],'\t', xi_3[i], '\t', xi_4[i], '\t', xi_5[i], '\t', xi_6[i], '\t', yi[i], '\t', yi_xi[i], '\t', yi_xi_2[i], '\t\t', yi_xi_3[i])
	else:
		print(xi[i], '\t', xi_2[i],'\t', xi_3[i], '\t', xi_4[i], '\t', xi_5[i], '\t', xi_6[i], '\t', yi[i], '\t', yi_xi[i], '\t', yi_xi_2[i], '\t', yi_xi_3[i])	

print('-----------------------------------------------------------------------------------------------------------------------------------')
print(sum(xi), '\t', sum(xi_2), '\t', sum(xi_3), '\t', sum(xi_4), '\t', sum(xi_5), '\t', sum(xi_6), '\t', sum(yi), '\t', round(sum(yi_xi), 1), ' ', round(sum(yi_xi_2), 1), '\t\t', round(sum(yi_xi_3), 1))
print('-----------------------------------------------------------------------------------------------------------------------------------')

#Составление нормальной системы
print()
print()
print('Нормальная система уравнений: ', end="")
system += ' {' +  f'{sum(x_0)} * c0 + {sum(xi)} * c1 + {sum(xi_2)} * c2 + {round(sum(xi_3), 2)} * c3 = {sum(yi)}\n'
system += ' {' +  f'{sum(xi)} * c0 + {sum(xi_2)} * c1 + {round(sum(xi_3), 2)} * c2 + {round(sum(xi_4), 2)} * c3 = {round(sum(yi_xi), 2)}\n'
system += ' {' +  f'{sum(xi_2)} * c0 + {round(sum(xi_3), 2)} * c1 + {round(sum(xi_4), 2)} * c2 + {round(sum(xi_5), 2)} * c3 = {round(sum(yi_xi_2), 2)}\n'
system += ' {' +  f'{round(sum(xi_3), 2)} * c0 + {round(sum(xi_4), 2)} * c1 + {round(sum(xi_5), 2)} * c2 + {round(sum(xi_6), 2)} * c3 = {round(sum(yi_xi_3), 2)}'

#Вывод нормальной системы
print()
print(system)

#Подсчет коэфициентов полинома
print()
matrix_A = np.array([[sum(x_0), sum(xi), sum(xi_2), sum(xi_3)], [sum(xi), sum(xi_2), sum(xi_3), sum(xi_4)], [sum(xi_2), sum(xi_3), sum(xi_4), sum(xi_5)], [sum(xi_3), sum(xi_4), sum(xi_5), sum(xi_6)]])
matrix_B = np.array([sum(yi), sum(yi_xi), sum(yi_xi_2), sum(yi_xi_3)])
answer = np.linalg.solve(matrix_A, matrix_B)

#Вывод коэфициентов полинома на экран
print('Коэфициенты :\n', 'c0 = ', round(answer[0], 3), ' \nc1 = ', round(answer[1], 3), ' \nc2 = ', round(answer[2], 3), ' \nc3 = ', round(answer[3], 3), sep='')

#Вывд полинома на экран
print()
print('Аппроксимирующий полином :', f'\nQ3(x) = {round(answer[0], 3)} + {round(answer[1], 3)} * x + ({round(answer[2], 3)}) * x^2 + ({round(answer[3], 3)}) * x^3')