failas = open('./paprastas-tekstas.txt')
tekstas = failas.read()
print(tekstas)

print(failas.closed)
failas.close()
print(failas.closed)
print(failas.read()) # klaida