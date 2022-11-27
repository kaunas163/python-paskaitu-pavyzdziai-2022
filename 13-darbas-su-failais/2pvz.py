failas = open('./paprastas-tekstas.txt')

nuskaitytas_tekstas = failas.read()
print('NUSKAITYTAS:', nuskaitytas_tekstas)
print()

kitas_tekstas = failas.read()
print('KITAS:', kitas_tekstas)

failas.close()