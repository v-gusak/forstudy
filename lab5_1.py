xi = [-0.25, 1.25, 2.00, 4.75, 6.55, 8.30, 9.48]
yi = [3.82, 2.94, 1.25, 5.85, 6.35, 4.25, 7.30]

rozd_razn_1 = []
rozd_razn_2 = []
rozd_razn_3 = []
rozd_razn_4 = []
rozd_razn_5 = []
rozd_razn_6 = []

polinom_Nut = ''
polinom_Lagr = ''

koefi_lagr = []
chisliteli = []
finale_lagr = []

chisliteli_finale = []
largange_in_x3 = 0
iksi_nut = []
nuton_in_x3 = 0

#Вывод значений X и Y на экран
print()
print('Xi = ', xi)
print('Yi = ', yi)
print()

#Вычисление раздельных разностей
for i in range(0, len(xi)):
	if(i != (len(xi) - 1)):
		rozd_razn_1.append(round((yi[i] - yi[i+1]) / (xi[i] - xi[i+1]), 2))

print('Раздельные разницы 1-го порядка -', rozd_razn_1)

for i in range(0, len(rozd_razn_1) - 1):
	rozd_razn_2.append(round((rozd_razn_1[i] - rozd_razn_1[i+1]) / (xi[i] - xi[i+2]), 2))

print('Раздельные разницы 2-го порядка -', rozd_razn_2)

for i in range(0, len(rozd_razn_2) - 1):
	rozd_razn_3.append(round((rozd_razn_2[i] - rozd_razn_2[i+1]) / (xi[i] - xi[i+3]), 2))

print('Раздельные разницы 3-го порядка -', rozd_razn_3)

for i in range(0, len(rozd_razn_3) - 1):
	rozd_razn_4.append(round((rozd_razn_3[i] - rozd_razn_3[i+1]) / (xi[i] - xi[i+4]), 2))

print('Раздельные разницы 4-го порядка -', rozd_razn_4)

for i in range(0, len(rozd_razn_4) - 1):
	rozd_razn_5.append(round((rozd_razn_4[i] - rozd_razn_4[i+1]) / (xi[i] - xi[i+5]), 4))

print('Раздельные разницы 5-го порядка -', rozd_razn_5)

for i in range(0, len(rozd_razn_5) - 1):
	rozd_razn_6.append(round((rozd_razn_5[i] - rozd_razn_5[i+1]) / (xi[i] - xi[i+6]), 4))

print('Раздельные разницы 6-го порядка -', rozd_razn_6)

#Построение полинома Ньютона с использованием раздельных разностей
polinom_Nut += '\n' + str(yi[0]) + ' + (' + str(rozd_razn_1[0]) + ')(x - (' + str(xi[0]) + '))' + ' + \n(' + str(rozd_razn_2[0])
polinom_Nut += ')(x - (' + str(xi[0]) + '))(x - ' + str(xi[1]) + ') + \n' + str(rozd_razn_3[0]) + '(x - (' + str(xi[0]) 
polinom_Nut += '))(x - ' + str(xi[1]) + ')(x - ' + str(xi[2]) + ') + \n(' + str(rozd_razn_4[0]) + ')(x - (' 
polinom_Nut += str(xi[0]) + '))(x - ' + str(xi[1]) + ')(x - ' + str(xi[2]) + ')(x - ' + str(xi[3]) + ')'
polinom_Nut += ' + \n' + str(rozd_razn_5[0]) + '(x - (' + str(xi[0]) + '))(x - ' + str(xi[1]) + ')(x - ' 
polinom_Nut += str(xi[2]) + ')(x - ' + str(xi[3]) + ')(x - ' + str(xi[4]) + ')' + ' + ' + '\n(' + str(rozd_razn_6[0])
polinom_Nut += ')(x - (' + str(xi[0]) + '))(x - ' + str(xi[1]) + ')(x - ' + str(xi[2]) + ')(x - ' + str(xi[3]) + ')'
polinom_Nut += '(x - ' + str(xi[4]) + ')(x - ' + str(xi[5]) + ')' 

#Вывод полинома Ньютона на экран
print()
print('P6(x) = ', polinom_Nut)

#Расчет коэфициентов для полинома Лагранжа
koef_lagr_0 = round(yi[0] / ((xi[0] - xi[1]) * (xi[0] - xi[2]) * (xi[0] - xi[3]) * (xi[0] - xi[4]) * (xi[0] - xi[5]) * (xi[0] - xi[6])), 5)
koef_lagr_1 = round(yi[1] / ((xi[1] - xi[0]) * (xi[1] - xi[2]) * (xi[1] - xi[3]) * (xi[1] - xi[4]) * (xi[1] - xi[5]) * (xi[1] - xi[6])), 5)
koef_lagr_2 = round(yi[2] / ((xi[2] - xi[0]) * (xi[2] - xi[1]) * (xi[2] - xi[3]) * (xi[2] - xi[4]) * (xi[2] - xi[5]) * (xi[2] - xi[6])), 5)
koef_lagr_3 = round(yi[3] / ((xi[3] - xi[0]) * (xi[3] - xi[1]) * (xi[3] - xi[2]) * (xi[3] - xi[4]) * (xi[3] - xi[5]) * (xi[3] - xi[6])), 5)
koef_lagr_4 = round(yi[4] / ((xi[4] - xi[0]) * (xi[4] - xi[1]) * (xi[4] - xi[2]) * (xi[4] - xi[3]) * (xi[4] - xi[5]) * (xi[4] - xi[6])), 5)
koef_lagr_5 = round(yi[5] / ((xi[5] - xi[0]) * (xi[5] - xi[1]) * (xi[5] - xi[2]) * (xi[5] - xi[3]) * (xi[5] - xi[4]) * (xi[5] - xi[6])), 5)
koef_lagr_6 = round(yi[6] / ((xi[6] - xi[0]) * (xi[6] - xi[1]) * (xi[6] - xi[2]) * (xi[6] - xi[3]) * (xi[6] - xi[4]) * (xi[6] - xi[5])), 5)

#Добавление коэфициентов в отдельный список
koefi_lagr.append(koef_lagr_0)
koefi_lagr.append(koef_lagr_1)
koefi_lagr.append(koef_lagr_2)
koefi_lagr.append(koef_lagr_3)
koefi_lagr.append(koef_lagr_4)
koefi_lagr.append(koef_lagr_5)
koefi_lagr.append(koef_lagr_6)

'''
print()
print('koefi = ', koefi_lagr)
'''

#Создание чистилелей для полинома Лагранжа
chislitel_0 = f'(x - {xi[1]})(x - {xi[2]})(x - {xi[3]})(x - {xi[4]})(x - {xi[5]})(x - {xi[6]})'
chislitel_1 = f'(x - ({xi[0]}))(x - {xi[2]})(x - {xi[3]})(x - {xi[4]})(x - {xi[5]})(x - {xi[6]})'
chislitel_2 = f'(x - ({xi[0]}))(x - {xi[1]})(x - {xi[3]})(x - {xi[4]})(x - {xi[5]})(x - {xi[6]})'
chislitel_3 = f'(x - ({xi[0]}))(x - {xi[1]})(x - {xi[2]})(x - {xi[4]})(x - {xi[5]})(x - {xi[6]})'
chislitel_4 = f'(x - ({xi[0]}))(x - {xi[1]})(x - {xi[2]})(x - {xi[3]})(x - {xi[5]})(x - {xi[6]})'
chislitel_5 = f'(x - ({xi[0]}))(x - {xi[1]})(x - {xi[2]})(x - {xi[3]})(x - {xi[4]})(x - {xi[6]})'
chislitel_6 = f'(x - ({xi[0]}))(x - {xi[1]})(x - {xi[2]})(x - {xi[3]})(x - {xi[4]})(x - {xi[5]})'

#Добавление полученных числителей в отдельный список
chisliteli.append(chislitel_0)
chisliteli.append(chislitel_1)
chisliteli.append(chislitel_2)
chisliteli.append(chislitel_3)
chisliteli.append(chislitel_4)
chisliteli.append(chislitel_5)
chisliteli.append(chislitel_6)

''''
print()
print('chisliteli = ', chisliteli)
'''

#Добавление частей полинома в отдельный список(готовый полином)
finale_lagr.append('')
for i in range(0, 7):
	if(i == 0 or i == 4):
		finale_lagr.append(f'({koefi_lagr[i]}) * {chisliteli[i]} + ')
	else:
		if(i == 5):
			finale_lagr.append(f'{koefi_lagr[i]} * {chisliteli[i]}')
		else:
			finale_lagr.append(f'{koefi_lagr[i]} * {chisliteli[i]} + ')

#Вывод полинома Лагранжа на экран
print()
print('L6(x) = ', finale_lagr[0])
for i in range(1,7):
	print(finale_lagr[i])

#Вычисление (x3 - xi) для полинома Ньютона
for i in range(0,7):
	iksi_nut.append(round((xi[3] - xi[i]), 4))

#Вычисление значения полинома Ньютона в точке x3
nuton_in_x3 += yi[0] + rozd_razn_1[0] * iksi_nut[0]
nuton_in_x3 += rozd_razn_2[0] * iksi_nut[0] * iksi_nut[1]
nuton_in_x3 += rozd_razn_3[0] * iksi_nut[0] * iksi_nut[1] * iksi_nut[2]
nuton_in_x3 += rozd_razn_4[0] * iksi_nut[0] * iksi_nut[1] * iksi_nut[2] * iksi_nut[3]
nuton_in_x3 += rozd_razn_5[0] * iksi_nut[0] * iksi_nut[1] * iksi_nut[2] * iksi_nut[3] * iksi_nut[4]
nuton_in_x3 += rozd_razn_6[0] * iksi_nut[0] * iksi_nut[1] * iksi_nut[2] * iksi_nut[3] * iksi_nut[4] * iksi_nut[5]

#Вычисление числителя для получения значения полинома Лагранжа в точке x3
chislitel_finale_0 = ((xi[3] - xi[1]) * (xi[3] - xi[2]) * (xi[3] - xi[3]) * (xi[3] - xi[4]) * (xi[3] - xi[5]) * (xi[3] - xi[6]))
chislitel_finale_1 = ((xi[3] - xi[0]) * (xi[3] - xi[2]) * (xi[3] - xi[3]) * (xi[3] - xi[4]) * (xi[3] - xi[5]) * (xi[3] - xi[6]))
chislitel_finale_2 = ((xi[3] - xi[0]) * (xi[3] - xi[1]) * (xi[3] - xi[3]) * (xi[3] - xi[4]) * (xi[3] - xi[5]) * (xi[3] - xi[6]))
chislitel_finale_3 = ((xi[3] - xi[0]) * (xi[3] - xi[1]) * (xi[3] - xi[2]) * (xi[3] - xi[4]) * (xi[3] - xi[5]) * (xi[3] - xi[6]))
chislitel_finale_4 = ((xi[3] - xi[0]) * (xi[3] - xi[1]) * (xi[3] - xi[2]) * (xi[3] - xi[3]) * (xi[3] - xi[5]) * (xi[3] - xi[6]))
chislitel_finale_5 = ((xi[3] - xi[0]) * (xi[3] - xi[1]) * (xi[3] - xi[2]) * (xi[3] - xi[3]) * (xi[3] - xi[4]) * (xi[3] - xi[6]))
chislitel_finale_6 = ((xi[3] - xi[0]) * (xi[3] - xi[1]) * (xi[3] - xi[2]) * (xi[3] - xi[3]) * (xi[3] - xi[4]) * (xi[3] - xi[5]))

#Добавление вычисленных числителей в отдельный список
chisliteli_finale.append(round(chislitel_finale_0, 2))
chisliteli_finale.append(round(chislitel_finale_1, 2))
chisliteli_finale.append(round(chislitel_finale_2, 2))
chisliteli_finale.append(round(chislitel_finale_3, 2))
chisliteli_finale.append(round(chislitel_finale_4, 2))
chisliteli_finale.append(round(chislitel_finale_5, 2))
chisliteli_finale.append(round(chislitel_finale_6, 2))

#Вычисление значения полинома Лагранжа в точке x3
for i in range(0, 7):
	largange_in_x3 += chisliteli_finale[i] * koefi_lagr[i]

#Вывод значения полинома Ньютона в точке x3
print()
print('P6(x3) = ', round(nuton_in_x3, 2))

#Вывод значения полинома Лагранжа в точке x3
print()
print('L6(x3) = ', round(largange_in_x3, 2))


