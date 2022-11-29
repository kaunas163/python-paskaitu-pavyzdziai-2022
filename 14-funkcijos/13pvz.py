def isvesti_masyva(komentaras, masyvas):
    print(komentaras)
    for elementas in masyvas:
        print('-', elementas)
    print()

skaiciai = [8, 7, 9]
zmones = ['Asta', 'Inga', 'Giedrius', 'Justas']

isvesti_masyva('Skaiciai', skaiciai)
isvesti_masyva('Zmones', zmones)