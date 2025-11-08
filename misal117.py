#117ci sual
#Aşağıda verilmiş siranın ilk N elementinin cəmini hesablayın. N – klaviaturadan daxil edilir. (1/3 + 2/9 + 3/27 + 4/81 + ...)
while True:
	n = int(input(" n-i yazın: "))
	s=0
	for i in range(1,n+1):
	    	x=i/3**i
	    	s+=x
     
	print(f' {s} \n')