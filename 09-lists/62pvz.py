import random

# tuscias list
skaiciai = []

# skaiciu generavimas
kiek = int(input("kiek skaiciu norite: "))
for sk in range(kiek):
    skaiciai.append(random.randint(1, 10))

# skaiciu isvedimas
print('sugeneruoti skaiciai:', skaiciai)

# skaiciu suma
suma = sum(skaiciai)
print('suma:', suma)

# skaiciu vidurkis
vidurkis = suma / len(skaiciai)
print('vidurkis:', round(vidurkis, 2))
