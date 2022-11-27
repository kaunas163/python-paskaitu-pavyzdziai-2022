# variantas nr 1

failas = open('./paprastas-tekstas.txt')
failas.read()
failas.close()

print(failas.closed) # True

# variantas nr 2

with open('./paprastas-tekstas.txt') as failas:
    failas.read()

print(failas.closed) # True