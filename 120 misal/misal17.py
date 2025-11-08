#17ci sual
#N natural ədədi verilmişdir. Bu ədəddə onun maksimal rəqəmi neçə dəfə iştirak etdiyini müəyyən edin. Məsələn, 673757 ədədində maksimal rəqəm 7 ədəddə 3 dəfə iştirak edir.
while True:
	n = list(input(" Ədədi yazın: "))
	print("  maksimal rəqəm: ",max(n))
	print(' ',n.count(max(n)), ' dəfə iştirak edib \n')