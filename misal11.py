#11ci sual
#N natural ədədi verilmişdir. Ədədin rəqəmlərinin cəmini və hasilini tapın.
while True:
	n = input(" Natural ədəd yazın: ")
	m=list(n)

	sum = 0
	for i in m:
		if i!=0:
			sum+=int(i)
		
	print(" Cəm: ",sum)

	hasil = 1
	for i in m:
		if i!=0:
			hasil*=int(i)
		
	print(" Hasil: ",hasil, '\n')