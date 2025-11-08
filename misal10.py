#10cu sual
#Ədəd o vaxt mükəmməl ədəd adlanır ki, onun bölənlərinin cəmi (özündən başqa) həmin ədədə bərabər olsun. Məsələn: 28=1+2+4+7+14. Klaviaturadan daxil edilən ədədin mükəmməl ədəd olduğunu yoxlamaq üçün proqram tərtib edin.
while True:
	x=int(input(' Ədədi yazın: '))
	y=[]
	for i in range(1,x):
		if x%i==0:
		     y.append(i)
       
	if sum(y)==x:
		print(" Bu ədəd mükəmməl ədəddir.\n")         
	else:
		print(" Bu ədəd mükəmməl ədəd deyil.\n")