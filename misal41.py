#41ci sual
#İki ədədin ƏBOB və ƏKOB-nu hesablayın
while True:
	from math import *
	a = int(input(" Ədəd yazın: "))
	b = int(input(" Ədəd yazın: "))

	ebob = gcd(a,b)
	print("ƏBOB:", ebob)

	ekob= (a*b)/ebob
	print("ƏKOB:", ekob, '\n')