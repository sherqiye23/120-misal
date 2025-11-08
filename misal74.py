#74cü sual
#Klaviaturadan istənilən ədəd daxil edilir. Bin funksiyasından istifadə etmədən həmin ədədi ikilik say sisteminə çevirən proqram tərtib edin
def ikilik(a):
	x=''
	while int(a) > 0:
		x+= str(int(a%2))
		a/=2
		z = x[::-1]
	print(f'0b{z}')

while True:
	a = input(' İkilik say sisteminə çevirmək üçün ədəd yazın: ')
	if a.isnumeric() == True:
		ikilik(int(a))