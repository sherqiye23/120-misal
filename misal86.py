#86cı sual
#Ədədlərdən ibarət siyahı verilmişdir. Bu siyahıda [a,b] intervalında yerləşən elementləri silin.
while True:
	def clear(list,a,b):
		del list[a:b+1]
		print(list)
	
	list=list(input(" Ədədlərdən ibarət siyahı yazın: "))
	a= int(input(" a-nı yazın: "))
	b= int(input(" b-ni yazın: "))

	clear(list,a,b)