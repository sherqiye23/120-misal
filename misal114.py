#114cü sual
#XİX əsrdə informasiyanın teleqraf vasitəsilə ötürülməsi üçün Morze əlifbası yaradılmışdır. Həmin əlifbanın 160 ildən çox yaşının olmasına baxmayaraq bu gün də istifadə olunmaqdadır. “Azerbaycan” sözünün kodlaşdırılması üçün proqram tərtib edin. Kömək: Lüğətlərdən istifadə edin.

def morseCode(mesaj):
    code = { 'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
 'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..'}
    morse_code = ""
    for x in mesaj:
        morse_code += code[x.upper()]
    return morse_code

mesaj = "Azerbaycan"
print(" Azerbaycan: ",morseCode(mesaj))