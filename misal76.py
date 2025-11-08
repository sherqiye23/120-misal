#76cı sual
#Sehrli tarix dedikdə gün və ay bir-birinə vurlduqda ilin sonuncu iki rəqəminə bərabər olur. Məsələn 9 oktyabr 1960. 9x10=60. XX əsrdə olan sehrli tarixləri tapmaq üçün proqram tərtib edin
print(" SEHRLİ İL PROQRAMI")
def function(a,b,c):
	for il in range(a,b,c):
		for ay in x:
			for gun in y:
				if ay * gun == il and len(str(il))==1:
					print(f"  {gun} - {ay} - 190{il}")

				elif ay * gun == il and len(str(il))==2:
					print(f"  {gun} - {ay} - 19{il}")
					
x = [1, 3, 5, 7, 8, 10, 12]
y = [y for y in range(1,32)]
function(1,100,1)

x = [4, 6, 9, 11]
y = [y for y in range(1,31)]
function(1,100,1)

x = [2]
y = [y for y in range(1,29)]
function(1,100,1)

x = [2]
y = [29]
function(4,97,4)