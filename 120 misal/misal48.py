#48ci sual
#1-dən 100-ə qədər  ədədlərin cəmini nəticə 150-dən kiçik olana qədər hesablayın
num=1
sum=0	
while num<=100:
	sum=sum+num
	num=num+1
	if sum<150:
		print(" ",sum)
	if sum+num > 150:
		break