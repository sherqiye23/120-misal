#70ci sual
#Klaviaturadan ingilis əlifbasının hərfi daxil edilir. Bu hərfin sait və ya samit olduğunu təyin edtmək üçün proqram yazın.
while True:
	sait = "aeiouAEİOU"
	samit = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

	herf = input("  Hərf yazın: ")

	if herf in sait:
		print(" Bu hərf saitdir.")

	elif herf in samit:
		print(" Bu hərf samitdir.")

	elif len(herf)>1:
		print(" 1 hərf yazın.")
	else:
		print(" Hərf ingilis əlifbasından olmalıdır.")