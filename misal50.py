#50ci sual
#Verilmiş 100 müxtəlif ədədin içində ən kiçik ədədi və onun ardıcıllıqdakı nömrəsini tapın
from random import*
a = [randint(1, 1000) for k in range(100)]
print(a)

b = min(a)
print(f' Ən kiçik ədəd: {b}')

print(" Ardıcıllıqdakı nömrəsi:", a.index(b, 1, 100))