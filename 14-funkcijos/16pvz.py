from random import randint

def atsitiktiniu_generavimas(kiek, min, max, masyvas):
    for i in range(kiek):
        masyvas.append( randint(min, max) )

def masyvo_isvedimas(komentaras, masyvas):
    print(komentaras)
    print(masyvas)
    print()

def sumos_paieska(masyvas):
    suma = 0
    for el in masyvas:
        suma += el
    print('suma:', suma)
    print()

skaiciai1 = []
skaiciai2 = []

atsitiktiniu_generavimas(10, 5, 10, skaiciai1)
atsitiktiniu_generavimas(5, 1, 10, skaiciai2)

masyvo_isvedimas('pirmi skaiciai', skaiciai1)
sumos_paieska(skaiciai1)

masyvo_isvedimas('antri skaiciai', skaiciai2)
sumos_paieska(skaiciai2)