#47ci sual
#1-dən 50-yə qədər ədədlərin cəmini həm For, həm də While dövr operatorlarının köməyilə hesablayıb nəticələri müqayisə edin

#with for
n=51
sum = 0
for i in range(1,n):
	sum+=i
print(" ",sum)

	
#with while			
num=1
sum=0	
while num<=50:
	sum += num
	num += 1
print(" ",sum)
