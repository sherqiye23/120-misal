#119cu sual
#Aşağıda verilmiş siranın ilk N elementinin cəmini hesablayın. N – klaviaturadan daxil edilir. (1+ 4/3 + 7/9 + 10/27 + 13/81 +...)
while True:
	n = int(input(" n-i yazın: "))
	s=1
	i=1
	while i<=n:
		s=s+(3*i+1)/3**i
		i=i+1

	print(f' {s} \n')