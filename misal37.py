#37ci sual
#[1,100] intervalında 10 təsadüfi ədəd yaradıb onların hasilini tapın

from random import *
a = [randint(1, 100) for k in range(10)]
print(a)

hasil = 1
for x in a:
	hasil*=x
print(" ",hasil)