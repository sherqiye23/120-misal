#14cü sual
#N natural ədədi verilmişdir. Bu ədədin yazılışında bütün 1 və 5 rəqəmləri silib, rəqəmlərin ardıcıllığını əvvəlki kimi saxlamaq lazımdır. Məsələn, 527012 ədədi 2702 ədədə çevriləcəkdir.

a = input(" Ədəd yazın: ")
b=list(a)
for i in a:
	if int(i) == 5 or int(i) == 1:
		b.remove(i)
	
print(" ","".join(b))
	