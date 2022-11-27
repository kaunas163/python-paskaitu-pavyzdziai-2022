failas = open('./paprastas-tekstas.txt')

nuskaitytas_tekstas = failas.read()
print('NUSKAITYTAS:', nuskaitytas_tekstas)
print()

failas.seek(0)
per_nauja_tekstas = failas.read()
print('PER NAUJA:', per_nauja_tekstas)

failas.close()