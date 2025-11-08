#118ci sual
#Aşağıda verilmiş siranın ilk N elementinin cəmini hesablayın. N – klaviaturadan daxil edilir. 
while True:
	n=int(input(" n-i yazın: "))
	x=0
	k=[ k for k in range(1,n+1,4)]
	for m in range(1,n+1):
		for i in range(2,n+2):
			for f in k:
				s=(int(i)**0.5)/f*(5**m)
				x+=s
 
	print(f' {x} \n')