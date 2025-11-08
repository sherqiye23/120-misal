#56cı sual
#Beşrəqəmli tam ədədinin daxil edin. Onun rəqəmlərinin kvadratlarının cəmini təyin edin
while True:
	def toplama(x):
		sum=0
		for i in x:
			sum+=int(i)**2
		return sum
		
	x = input("  5rəqəmli ədəd yazın: ")
	if len(x)==5:
		print('  ',toplama(x), '\n')