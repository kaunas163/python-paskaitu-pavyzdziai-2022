pirmas = int( input('Pirmas skaicius: ') )
antras = int( input('Antras skaicius: ') )

if pirmas > antras:
    print(pirmas, 'didesnis nei', antras)
elif antras > pirmas:
    print(antras, 'didesnis uz', pirmas)
else:
    print('skaiciai lygus')
