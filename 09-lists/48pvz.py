import random

kiek = int(input('kiek skaiciu sukurti? '))
skaiciai = []

for sk in range(kiek):
    skaiciai.append(random.randint(1, 100))

print(skaiciai)