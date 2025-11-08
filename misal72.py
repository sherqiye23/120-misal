#72ci sual
#Klaviaturadan gün və ayın nömrəsi daxil edilir. Həmin günün ilin hansı fəslinə uyğun olduğunu təyin etmək üçün proqram tərtib edin

while True:
	gün = int(input(' Günü yazın: '))
	ay = int(input(' Ayı yazın: '))

	if (31>=gün>=20 and ay==3) or (30>=gün>=1 and ay==4) or (31>=gün>=1 and ay==5) or (20>=gün>=1 and ay==6):
		print('\n YAZ \n')
	
	elif (30>=gün>=21 and ay==6) or (31>=gün>=1 and ay==7) or (31>=gün>=1 and ay==8) or (22>=gün>=1 and ay==9):
		print('\n YAY \n')
	
	elif (30>=gün>=23 and ay==9) or (31>=gün>=1 and ay==10) or (30>=gün>=1 and ay==11) or (21>=gün>=1 and ay==12):
		print('\n PAYIZ \n')
	
	elif (31>=gün>=22 and ay==12) or (31>=gün>=1 and ay==1) or (29>=gün>=1 and ay==2) or (19>=gün>=1 and ay==3):
		print('\n QIŞ \n')