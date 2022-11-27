eilutes = []

with open('./paprastas-tekstas.txt') as failas:
    while True:
        eilute = failas.readline().rstrip('\n')
        if not eilute:
            break
        print('nuskaityta eilute:', eilute)
        eilutes.append(eilute)

print(eilutes)