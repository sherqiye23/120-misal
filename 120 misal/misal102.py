#102ci sual
#İstənilən il daxil edin. Bu ilin uzun il (fevral 29 gün olduqda il uzun il sayılır) olduğunu və hansı əsrə aid olduğunu təyin edin
while True:
	def əsr(n):
		a = int(n[0]+n[1])
		print(' Əsr: ',a+1)
	
	n = input(' İl yazın: ')
	if int(n)%4==0:
		print(' Uzun ildi')
	else:
		print(' Uzun il deyil')
	əsr(n)