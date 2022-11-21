preke1 = dict(
    pavadinimas = 'piestukas',
    kaina = 0.99,
    kiekis = 142
)

preke2 = dict(
    pavadinimas = 'sasiuvinys',
    kaina = 1.49,
    kiekis = 241
)

print('pirma preke:', preke1)
print('antra preke:', preke2)

if preke1['kiekis'] > preke2['kiekis']:
    print('pirmos prekes daugiau vienetu')
elif preke2['kiekis'] > preke1['kiekis']:
    print('antros prekes daugiau vienetu')
else:
    print('abieju prekiu vienodai')