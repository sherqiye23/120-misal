#103cü sual
#Həqiqi A ədədi verilmişdir. Aşağıdakı qayda ilə f(A)-nı hesablayın: əgər  x ≤ 0, onda f(x) = 0 ; əgər  0 < x < 1 isə, onda f(x) = x^2 − x , əks halda : f(x) = x^2 − sin(πx^2).
while True:
	from math import *
	def function(x):
		if x<=0:
			y=0
		
		elif 0<x<1:
			y=x**2-x
		
		else:
			y=x**2 - sin(pi*x**2)
		
		print(" ",y)
		
	a = float(input(" A-nın qiymətini yazın: "))
	function(a)