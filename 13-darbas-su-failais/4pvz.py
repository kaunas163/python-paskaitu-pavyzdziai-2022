failas = open('./paprastas-tekstas.txt')

nuskaitytas_tekstas = failas.read()
print('NUSKAITYTAS:', nuskaitytas_tekstas)
print()

failas.seek(16)
per_nauja_tekstas = failas.read()
print('NUO 16-OS VIETOS:', per_nauja_tekstas)

failas.close()