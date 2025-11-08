#39cu sual
#1-dən 100-ə qədər 3-ə tam bölünməyən ədədlərin cəmini hesablayın

y = [y for y in range(1, 101) if y%3 != 0]
print(" ", y)

sum = 0
for x in y:
	sum+=x
print(" ", sum)