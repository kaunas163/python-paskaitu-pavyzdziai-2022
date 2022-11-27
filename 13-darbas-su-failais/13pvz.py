with open('./paprastas-tekstas.txt') as failas:
    visas_tekstas = failas.readlines()
    print('VISAS TEKSTAS:', visas_tekstas)
    sutvarkytas_tekstas = [ eilute.rstrip('\n') for eilute in visas_tekstas ]
    print('SUTVARKYTAS TEKSTAS:', sutvarkytas_tekstas)