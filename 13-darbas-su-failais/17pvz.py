eilutes = []

with open('./paprastas-tekstas.txt') as failas:
    for eilute in failas:
        eilute = eilute.rstrip('\n')
        print('nuskaityta eilute:', eilute)
        eilutes.append(eilute)

print(eilutes)