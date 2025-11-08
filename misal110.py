#110cu sual
#N ədədini daxil edin. 1³+2³+...+N³ cəmini hesablayın.
while True:
	from math import *
	n = int(input(" Rəqəmi yazın: "))
	m = [k**3 for k in range(1, n+1)]
	p = sum(m)
	print(f'  {p} \n')