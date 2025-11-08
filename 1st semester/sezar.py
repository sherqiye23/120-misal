k=2

kod="abc ggg"

əlifba="abcdefghijklmnopqrstuvwxyz"

sezarda_kod=''

for a in kod:
    
    for b in əlifba:
        
        if a==b:
            
           sıra=əlifba.index(b)
           
           sıra+=k
           
           sezarda_kod+=əlifba[sıra%len(əlifba)]
           
print(sezarda_kod)