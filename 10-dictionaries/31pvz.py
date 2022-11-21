preke = {
    'pavadinimas': 'piestukas',
    'kodas': 'ASFSDG458485',
    'kaina': 2.99,
    'kiekis_sandelyje': 451
}

print('preke:', preke, '\n')
print('pardavus preke galetume uzdirbti:',
    (preke['kaina'] * preke['kiekis_sandelyje']))