#98ci sual
#Cüt sayda təsadüfi ədədlərdən ibarət siyahı yaradın. Bu siyahının 1-ci yarısının elementləri ilə 2-ci yarısının elementlərinin yerini dəyişməklə alınan siyahını ekrana çıxarın
from random import*
a = [2* randint(1,100) for a in range(8)]
print(a)
ilkYarı = (a[:round((len(a))/2)])
ikinciYarı = (a[round(len(a)/2) :])
c = ikinciYarı + ilkYarı
print(c)