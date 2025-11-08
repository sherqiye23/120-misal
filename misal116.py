#116cı sual
'''Nyuton metodu ilə klaviaturadan daxil edilmiş ədədin kvadrat kökünün təqribi tapılması üçün proqram tərtib edin. Qeyd: Alqoritm aşağıdakı iterasiyalar ardıcıllığına əsaslanır: Tutaq ki, verilmiş X ədədinin kvadrat kökünü təqribi hesablamaq lazımdır. 
A1=1 (və ya A1-i kvadratı həmin ədədi aşmayan ədəd götürmək olar)
A2=0.5 *(A1 + X/A1)
A3=0.5* (A2 + X/A2)
A/n+1/=0.5*(An+X/An)
Verilmiş dəqiqliklə klaviaturadan daxil edilmiş X ədədinin kvadrat kökünü təqribi hesablamaq üçün proqram tərtib edin.'''
while True:
	x = int(input(' Ədəd yazın: '))
	a = x-1
	for i in range(100):
		a = 0.5*(a + x/a)
	print(f' Kvadrat kökü: {a} \n')