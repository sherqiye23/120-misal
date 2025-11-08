#38ci sual
#1-dən 100-ə qədər 5-ə tam bölünən ədədlərin cəmi ilə 5-ə tam bölünməyən ədədlərin cəminin fərqini hesablayın
def toplama(n):
	sum=0
	for x in n:
		sum+=x
	return sum
	
a = [a for a in range(1,101) if a%5 ==0]
print(a)

b = [b for b in range(1, 101) if b%5 !=0]
print(b)

print(" ",toplama(a) - toplama(b))