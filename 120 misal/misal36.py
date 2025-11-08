#36cı sual
#[1,100] intervalında 10 təsadüfi ədəd yaradıb onları cəmləyin

from random import *
a = [randint(1, 100) for k in range(10)]
print(a)

sum = 0
for x in a:
	sum+=x
print(" ", sum)