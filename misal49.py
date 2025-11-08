#49cu sual
#1-dən 100-ə qədər  ədədlərin hasilini nəticə 1500-dən kiçik olana qədər hesablayın
num=1
hasil=1	
while num<=100:
	hasil*=num
	num=num+1
	if hasil<1500:
		print(" ",hasil)
	if hasil*num > 1500:
		break