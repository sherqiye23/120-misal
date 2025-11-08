#23cü sual
#N natural ədədi verilmişdir. Onun bölənlərini artma ardıcıllığı ilə ekrana çıxarın. 
while True:
	x=int(input(" Ədədi yazın: "))
	y=[]
	for i in range(1,x+1):
		if x%i==0:
			y.append(i)
	
	print(y, '\n')