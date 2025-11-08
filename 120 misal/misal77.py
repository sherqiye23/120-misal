#77ci sual
#Sətir şəklində simvollar ardıcıllığı verilmişdir. Həmin sətrin etibarlı parol ola biləcəyini yoxlayın. Qeyd: Etibarlı parolda həm minimum 1 böyük, minimum 3 kiçik, minimum 2 rəqəm və minimum 1 simvolun(həərf və rəqəm olmayan) olması tələb olunur.
while True:
	def etibarliparol(n):
		a="QÜERTYUİOPÖĞASDFGHJKLIƏZXCVBNMÇŞW"
		b="qüertyuiopöğasdfghjklıəzxcvbnmçşw"
		c="0123456789"
		boyuk,kicik,reqem,simvol = 0,0,0,0
		for i in n:
			if i in a:
				boyuk += 1
			if i in b:
				kicik += 1
			if i in c:
				reqem += 1
			else:
				simvol += 1
		if boyuk >= 1 and kicik >= 1 and reqem >= 3 and simvol >= 2:
			print("Etibarlı paroldur\n")
		else:
			print("Etibarlı parol deyil\n")
			
	n = input(' Parolunuzu yazın: ')

	etibarliparol(n)