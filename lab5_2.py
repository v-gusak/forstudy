from math import factorial 

xi = [-0.25, 1.25, 2.75, 4.25, 5.75, 7.25]
yi = [3.96, 2.97, 1.85, 5.89, 6.30, 4.21]

h = 1.5

#Вывод значений X и Y на экран
print()
print('Xi = ', xi)
print('Yi = ', yi)
print()

kon_razn_1 = []
kon_razn_2 = []
kon_razn_3 = []
kon_razn_4 = []
kon_razn_5 = []

kon_razn_vtor_1 = []
kon_razn_vtor_2 = []
kon_razn_vtor_3 = []
kon_razn_vtor_4 = []
kon_razn_vtor_5 = []

polinom_Nut_1 = ''
polinom_Nut_2 = ''

polinom_Nut_1_in_x4 = 0
polinom_Nut_2_in_x4 = 0

#Вычисление конечных разностей с 1-го по n-ый порядок
for i in range(0, len(yi) - 1):
	kon_razn_1.append(round(yi[i+1] - yi[i], 2))

for i in range(0, len(kon_razn_1) - 1):
	kon_razn_2.append(round(kon_razn_1[i+1] - kon_razn_1[i], 2))

for i in range(0, len(kon_razn_2) - 1):
	kon_razn_3.append(round(kon_razn_2[i+1] - kon_razn_2[i], 2))

for i in range(0, len(kon_razn_3) - 1):
	kon_razn_4.append(round(kon_razn_3[i+1] - kon_razn_3[i], 2))

for i in range(0, len(kon_razn_4) - 1):
	kon_razn_5.append(round(kon_razn_4[i+1] - kon_razn_4[i], 2))

#Вывод конечных разностей на экран
print('Конечные разницы 1-го порядка - ', kon_razn_1)
print('Конечные разницы 2-го порядка - ', kon_razn_2)
print('Конечные разницы 3-го порядка - ', kon_razn_3)
print('Конечные разницы 4-го порядка - ', kon_razn_4)
print('Конечные разницы 5-го порядка - ', kon_razn_5)

#Составление полинома Ньтона с конечными разницами первого рода
polinom_Nut_1 += f'\n{yi[0]} + ({kon_razn_1[0] / (factorial(1) * h)})(x - ({xi[0]})) + \n'
polinom_Nut_1 += f'({round(kon_razn_2[0] / (factorial(2) * (h**2)), 2)})(x - ({xi[0]}))(x - {xi[1]}) + \n'
polinom_Nut_1 += f'({round(kon_razn_3[0] / (factorial(3) * (h**3)), 2)})(x - ({xi[0]}))(x - {xi[1]})(x - {xi[2]}) + \n'
polinom_Nut_1 += f'({round(kon_razn_4[0] / (factorial(4) * (h**4)), 2)})(x - ({xi[0]}))(x - {xi[1]})(x - {xi[2]})(x - {xi[3]}) + \n'
polinom_Nut_1 += f'({round(kon_razn_5[0] / (factorial(5) * (h**5)), 2)})(x - ({xi[0]}))(x - {xi[1]})(x - {xi[2]})(x - {xi[3]})(x - {xi[4]})'

#Составление полинома Ньтона с конечными разницами второго рода
polinom_Nut_2 += f'\n{yi[-1]} + ({round(kon_razn_1[-1] / (factorial(1) * h), 2)})(x - {xi[-1]}) + \n'
polinom_Nut_2 += f'({round(kon_razn_2[-1] / (factorial(2) * (h**2)), 2)})(x - {xi[-1]})(x - {xi[-2]}) + \n'
polinom_Nut_2 += f'({round(kon_razn_3[-1] / (factorial(3) * (h**3)), 2)})(x - {xi[-1]})(x - {xi[-2]})(x - {xi[-3]}) + \n'
polinom_Nut_2 += f'({round(kon_razn_4[-1] / (factorial(4) * (h**4)), 2)})(x - {xi[-1]})(x - {xi[-2]})(x - {xi[-3]})(x - {xi[-4]}) + \n'
polinom_Nut_2 += f'({round(kon_razn_5[-1] / (factorial(5) * (h**5)), 2)})(x - {xi[-1]})(x - {xi[-2]})(x - {xi[-3]})(x - {xi[-4]})(x - {xi[-5]})'

#Вывод полинома Ньютона с конечными разницами первого рода
print()
print('1) N5(x) = ', polinom_Nut_1)

#Вывод полинома Ньютона с конечными разницами второго рода
print()
print('2) N5(x) = ', polinom_Nut_2)

#Вычисление значения полинома Ньтона с конечными разницами первого рода в точке x4
polinom_Nut_1_in_x4 += yi[0]+(((kon_razn_1[0])/(factorial(1)*h))*(xi[4] - xi[0]))
polinom_Nut_1_in_x4 += (((kon_razn_2[0])/(factorial(2)*(h**2)))*(xi[4] - xi[0])*(xi[4] - xi[1]))
polinom_Nut_1_in_x4 += (((kon_razn_3[0])/(factorial(3)*(h**3)))*(xi[4] - xi[0])*(xi[4] - xi[1])*(xi[4] - xi[2]))
polinom_Nut_1_in_x4 += (((kon_razn_4[0])/(factorial(4)*(h**4)))*(xi[4] - xi[0])*(xi[4] - xi[1])*(xi[4] - xi[2])*(xi[4] - xi[3]))
polinom_Nut_1_in_x4 += (((kon_razn_5[0])/(factorial(5)*(h**5)))*(xi[4] - xi[0])*(xi[4] - xi[1])*(xi[4] - xi[2])*(xi[4] - xi[3])*(xi[4] - xi[4]))

#Вывод на экран значения полинома Ньтона с конечными разницами первого рода в точке x4
print()
print('1) N5(x4) = ', round(polinom_Nut_1_in_x4, 2))

#Вычисление значения полинома Ньтона с конечными разницами второго рода в точке x4
polinom_Nut_2_in_x4 += yi[-1]+(((kon_razn_1[-1])/(factorial(1)*h))*(xi[4] - xi[-1]))
polinom_Nut_2_in_x4 += (((kon_razn_2[-1])/(factorial(2)*(h**2)))*(xi[4] - xi[-1])*(xi[4] - xi[-2]))
polinom_Nut_2_in_x4 += (((kon_razn_3[-1])/(factorial(3)*(h**3)))*(xi[4] - xi[-1])*(xi[4] - xi[-2])*(xi[4] - xi[-3]))
polinom_Nut_2_in_x4 += (((kon_razn_4[-1])/(factorial(4)*(h**4)))*(xi[4] - xi[-1])*(xi[4] - xi[-2])*(xi[4] - xi[-3])*(xi[4] - xi[-4]))
polinom_Nut_2_in_x4 += (((kon_razn_5[-1])/(factorial(5)*(h**5)))*(xi[4] - xi[-1])*(xi[4] - xi[-2])*(xi[4] - xi[-3])*(xi[4] - xi[-4])*(xi[4] - xi[-5]))

#Вывод на экран значения полинома Ньтона с конечными разницами второго рода в точке x4
print()
print('2) N5(x4) = ', round(polinom_Nut_2_in_x4, 2))