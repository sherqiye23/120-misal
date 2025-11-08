#109cu sual
#N ədədini daxil edin. 1²+2²+...+N² cəmini hesablayın.
while True:
	from math import *
	n = int(input(" Rəqəmi yazın: "))
	m = [k**2 for k in range(1, n+1)]
	p = sum(m)
	print(f'  {p} \n')