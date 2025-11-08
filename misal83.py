#83cü sual
#N-rəqəmli tam ədəd verilmişdir. Bu ədəddə tək rəqəmlərin  həndəsi ortasını tapın.
while True:
	def vurma(list):
		hasil = 1
		for i in list:
			hasil*=i
		return hasil

	n = input(" Rəqəm yazın: ")
	tek_ededler = []
	for i in n:
		if int(i)==1 or int(i)%2!=0:
			tek_ededler.append(int(i))

	x = vurma(tek_ededler)

	hendesi_orta = int(x)**(1/len(tek_ededler))

	print(f"Həndəsi orta: {hendesi_orta}\n")