#73cü sual
#Klaviaturadan gün ,ay və il sətir formatında daxil edilir. Alınmış tarixə əsasən növbəti günü təyin etmək üçün proqram tərtib edin
def yoxlama(gun,ay,il):
    y = [4, 6, 9, 11]
    if ay<1 or ay>12 or gun>31:
        return 'Səhvdi'
    if ay in y and gun>30:
        return 'Səhvdi'
    if ay==2:
        if il%4==0 and gun > 29:
            return 'Səhvdi'
        if il%4!=0 and gun>28:
            return 'Səhvdi'
    return True

def calendar(gun,ay,il):
    if yoxlama(gun,ay,il) == True:
        if yoxlama(gun+1,ay,il) == True:
            return [gun+1,ay,il]
        elif yoxlama(gun+1,ay,il) == False and yoxlama(1,ay+1,il) == True:
        	return [1,ay+1,il]
        else:
            return [1,1,il+1]
            
    else:
        return 'Belə tarix yoxdur\n'

while True:
	gun = int(input('Günü yazın: '))
	ay = int(input('Ayı yazın: '))
	il = int(input('İli yazın: '))
	print(calendar(gun,ay,il), '\n')