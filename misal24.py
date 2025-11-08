#24cü sual
#N natural ədədi verilmişdir.  Onun sadə ədəd olduğunu yoxlayın.
while True:
	def sade(n):
		x=[]
		i = [i for i in range(1,n)]
		for c in i:
			if n%int(c)==0:
				x.append(c)
			
		if n == 1:
			return " Nə sadədir, nə də mürəkkəb \n"
		elif len(x)>1:
			return " Sadə deyil\n"
		elif len(x)==1:
			return " Sadədir\n"

	n = int(input('Ədəd yazın: '))
	print(sade(n))