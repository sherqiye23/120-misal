#19cu sual
#Verilən N ədədən böyük olmayan və rəqəmləri artan ardıcıllığı ilə düzülən bütün natural ədədləri çıxışa verin.
def artan(x):
	for i in range(len(str(x))-1):
		if int(str(x)[i])<int(str(x)[i+1]):
			pass
		
		else:
			return False
	return True
		

s=[]
n = input(" Ədəd yazın: ")
for a in range(1,1+int(n)):
	if artan(a)==True:
		s.append(a)
		
print(s)

