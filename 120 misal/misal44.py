#44cü sual
#Factorial funksiyasından istifadə etmədən Kombinezonu hesablayın. n və m – daxil edilir.
while True:
	def faktorial(x):
		factorial = 1
		for i in range(1, x+1):
			factorial*=i
		return factorial
	
	n = int(input(" n-i yazın: "))
	m = int(input(" m-i yazın: "))

	kombinezon = faktorial(n)/(faktorial(m)*faktorial(abs(n-m)))
	print(" Kombinezon:",kombinezon, '\n')