#115ci sual
#Ən qədim şifrələmə metodlarından biri Yuli Sezara məxsusdur. Onun şifrələmə metodunda hər bir hərf 3 mövqe sağa sürüşdürməklə alınan hərflə kodlaşdırılır. Məsələn: A -> D, B->E, C->F və s. Əlifbanın sonuncu 3 hərfi isə əvvələ sürüşdürülür. Yəni X->A, Y->B, Z->C olur. Rəqəmlər və digər xüsusi simvollar şifrələnmir. Bu şifrələmə metodundan istifadə etməkə “Azerbaycan” sözünün kodlaşdırılması üçün proqram tərtib edin.
def sezarCode(söz):
    alphabet = {"a":"d", "b":"e", "c":"f", "d":"g", "e":"h", "f":"i",
     "g":"j", "h":"k", "i":"l", "j":"m", "k":"n", "l":"o", "m":"p",
     "n":"q", "o":"r", "p":"s", "q":"t", "r":"u", "s":"v", "t":"w", 
     "u":"x", "v":"y", "w":"z", "x":"a", "y":"b", "z":"c"}
    
    sezar_code = ""
    for x in söz:
        sezar_code += alphabet[x.lower()]
    return sezar_code

söz = "Azerbaycan"
print(" Azerbaycan: ",sezarCode(söz))