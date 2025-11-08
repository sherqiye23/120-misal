#42ci sual
#Factorial funksiyasından istifadə etmədən N!-i hesablayın. N – daxil edilir.
while True:
	def faktorial(x):
		factorial = 1
		for i in range(1, x+1):
			factorial*=i
		return factorial
	
	n = int(input(" n-i yazın: "))
	print(" ",f"{n}-in faktorialı:",faktorial(n))