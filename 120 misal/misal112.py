#112ci sual
#N ədədini daxil edin. 1²+2²+...+N² cəminin  1³+2³+...+N³ cəminin neçə faizini təşkil etdiyini hesablayın.
while True:
	from math import *
	n = int(input(" Rəqəmi yazın: "))

	p = 1
	m = [k**2 for k in range(1, n+1)]
	p = sum(m)

	q = 1
	x = [k**3 for k in range(1, n+1)]
	q = sum(x)

	z = (p/q)*100
	print(f' {z} \n')