skaiciai = [8, 5, 7, 4, 2, 3]

lyginiu_suma = 0
lyginiu_kiekis = 0

for skaicius in skaiciai:
    if skaicius % 2 == 0:
        lyginiu_suma += skaicius
        lyginiu_kiekis += 1

vidurkis = round(lyginiu_suma / lyginiu_kiekis, 2)

print('skaiciai:', skaiciai)
print('lyginiu suma:', lyginiu_suma)
print('lyginiu kiekis:', lyginiu_kiekis)
print('lyginiu vidurkis:', vidurkis)