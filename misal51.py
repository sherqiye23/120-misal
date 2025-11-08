#51ci sual
#Verilmiş 100 müxtəlif ədədin içində ən böyük ədədi və onun ardıcıllıqdakı nömrəsini tapın
from random import*
a = [randint(1, 1000) for k in range(100)]
print(a)

b = max(a)
print(f' Ən böyük ədəd: {b}')

print(" Ardıcıllıqdakı nömrəsi:", a.index(b, 1, 100))