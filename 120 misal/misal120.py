#120ci sual
#Aşağıda verilmiş siranın ilk N elementinin cəmini hesablayın. N – klaviaturadan daxil edilir. (1-2/3 + 4/9 +...)
while True:
	n = int(input(" n-i yazın: "))
	s = -1/3
	i = 1
	if n == 0 or n == 1:
		s = n
	else:
		while i <= n - 1:
			s += 2*i/3**i
			i += 1

	print(f' {s} \n')