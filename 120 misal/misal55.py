#55ci sual
#Beşrəqəmli tam ədədinin daxil edin. Onun rəqəmlərinin hasilini rəqəmlərini cəminə bölüb tam hissəni təyin edin.
while True:
	def hasilHesab(x):
		hasil=1
		for i in x:
			hasil*=int(i)
		return hasil
	
	def toplama(x):
		sum=0
		for i in x:
			sum+=int(i)
		return sum
		
	x = input("  5rəqəmli ədəd yazın: ")
	if len(x)==5:
		print('  ',hasilHesab(x)//toplama(x), '\n')