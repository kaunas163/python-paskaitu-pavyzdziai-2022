pazymiai = [7, 4, 8, 7, 9, 6, 2, 5]

teigiami = []
neigiami = []

for paz in pazymiai:
    if paz >= 5:
        teigiami.append(paz)
    else:
        neigiami.append(paz)

print('pazymiai:', pazymiai)
print('teigiami pazymiai:', teigiami)
print('neigiami pazymiai:', neigiami)