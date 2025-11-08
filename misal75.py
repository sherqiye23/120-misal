#75ci sual
#Klaviaturadan 16-lıq say sistemində istənilən ədəd daxil edilir. İnt funksiyasından istifadə etmədən həmin ədədi onluq say sisteminə çevirən proqram tərtib edin
def on6lıq(a):
    listNum = '0123456789'
    dict = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
    x = 0
    l = len(a)-1
    index = 0
    while index < len(a):
        if a[index] in listNum:
        	x += int(a[index])*16**l
        elif a[index] in dict:
        	x += dict[a[index]]*16**l
        else:
        	return False
        l -= 1
        index += 1
    return x

while True:
    num = input(' 16-lıq say sistemində ədəd yazın: ')
    if on6lıq(num) != False:
    	print(on6lıq(num), '\n')