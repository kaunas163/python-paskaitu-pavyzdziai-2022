def masyvo_isvedimas(masyvas):
    tekstu = ', '.join(map(str, masyvas))
    print('DUOMENYS:', tekstu)

def sumos_paieska(skaiciu_masyvas):
    suma = 0
    for sk in skaiciu_masyvas:
        suma += sk
    print('gauta suma:', suma)
    print()

skaiciai1 = [6, 8, 6, 10, 8, 7]
skaiciai2 = [23, 65, 74, 28]

masyvo_isvedimas(skaiciai1)
sumos_paieska(skaiciai1)

masyvo_isvedimas(skaiciai2)
sumos_paieska(skaiciai2)