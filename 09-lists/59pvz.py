pazymiai = [7, 4, 8, 7, 9, 6, 2, 5]

kiek_neigiamu = 0

for paz in pazymiai:
    if paz < 5:
        kiek_neigiamu += 1

print('pazymiai:', pazymiai)
print('neigiamu pazymiu kiekis:', kiek_neigiamu)