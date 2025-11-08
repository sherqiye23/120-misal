#25ci sual
#N natural ədədi verilmişdir.  N ədəddən kiçik olan sadə ədədləri çıxışa verin.
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
	list=[]
	for i in range(n):
		if sade(i) == " Sadədir\n":
			list.append(i)
	print('   ',list)