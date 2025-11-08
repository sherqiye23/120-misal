#84cü sual
#N-rəqəmli tam ədəd verilmişdir.Bu ədəddə iki dəfə ardıcıl olaraq 0-rəqəminin olub-olmadığıını təyin edin.
while True:
	n=input(" Ədəd yazın: ")
	list = []
	for i in range(len(n)-1):
		if n[i]==n[i+1]=='0':
			list.append("turyu")
		
	if len(list) == 2:
		print(' 2 dəfə ardıcıl 0 var \n')
	else:
		print(' No \n')