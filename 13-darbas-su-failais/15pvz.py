with open('./paprastas-tekstas.txt') as failas:
    print( type( failas.read() ) )
    failas.seek(0)
    print( type( failas.readline() ) )
    failas.seek(0)
    print( type( failas.readlines() ) )