#113cü sual
#Π-ədədinin təqribi hesablanması üçün aşağıdakı düsturdan istifadə etməklə ilk 15 toplanandan istifadə etməklə onun qiymətini hesablayın:
pi = 3
x = 0
for i in range(2, 17, 2):
	pi += ((-1)**x)*(4/(i*(i+1)*(i+2)))
	x+=1
print("  ",pi)
