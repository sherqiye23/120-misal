#40cu sual
#1-dən 100-ə qədər 3-ə tam bölünən ədədlərin cəminin 3-ə tam bölünməyən ədədlərin cəminin neçə faizi olduğunu hesablayın
def toplama(n):
	sum=0
	for x in n:
		sum+=x
	return sum
	
a = [a for a in range(1, 101) if a%3 ==0]
print(a)

b = [b for b in range(1, 101) if b%3 !=0]
print(b)

print(' ',toplama(a)/toplama(b)*100)