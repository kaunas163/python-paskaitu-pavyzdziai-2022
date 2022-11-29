def skaiciu_suma(masyvas):
    suma = 0
    for sk in masyvas:
        suma += sk
    return suma

skaiciai = [7, 8, 5, 3, 5, 4, 1]

suma = skaiciu_suma(skaiciai)
vidurkis = suma / len(skaiciai)

print('skaiciai:', skaiciai)
print('suma:', suma)
print('vidurkis:', vidurkis)