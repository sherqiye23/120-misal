#82ci sual
#N-rəqəmli tam ədəd verilmişdir. Bu ədəddə cüt rəqəmlərin  həndəsi ortasını tapın.
while True:
	def vurma(list):
		hasil = 1
		for i in list:
			hasil*=i
		return hasil

	n = input(" Rəqəm yazın: ")
	cut_ededler = []
	for i in n:
		if int(i)%2==0:
			cut_ededler.append(int(i))

	x = vurma(cut_ededler)

	hendesi_orta = int(x)**(1/len(cut_ededler))

	print(f"Həndəsi orta: {hendesi_orta}\n")