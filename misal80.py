#80ci sual
#N-rəqəmli tam ədəd verilmişdir. Bu ədəddə cüt rəqəmlərin  ədədi ortasını tapın.
while True:
	n = list(input(" Ədəd yazın: "))
	z=[]
	for i in n:
		if int(i)%2==0:
			z.append(int(i))
		
	print(z)
	d=sum(z)/len(z)
	print(f" Ədədi orta: {d} \n")