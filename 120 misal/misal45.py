#45ci sual
#F(0)=F(1)=1 və F(n)=F(n-1)+F(n-2) şəklində təyin olunan Fibonaççi ədədlərini hesablayın. n=100
list=[]
x = 0
y = 1
for i in range(50):
	x += y
	y += x
	list.append(x)
	list.append(y)

print(' 100cü Fibonacci ədədi: ', list[99])