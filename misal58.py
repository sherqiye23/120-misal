#58ci sual
#Beşrəqəmli tam ədədinin daxil edin. Onun rəqəmlərinin kubları cəmini rəqəmlərin kvadratları cəminə bölüb alınan qalığı təyin edin.
while True:
	def kubToplama(x):
		sum=0
		for i in x:
			sum+=int(i)**3
		return sum
		
	def kvadratToplama(x):
		sum=0
		for i in x:
			sum+=int(i)**2
		return sum
		
	x = input("  5rəqəmli ədəd yazın: ")
	if len(x)==5:
		print(' Alınan qalıq:', kubToplama(x)%kvadratToplama(x))