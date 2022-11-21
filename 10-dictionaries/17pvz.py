studentas = dict(
    vardas = 'Tomas',
    pavarde = 'Tomauskas',
    amzius = 23,
    ugis = 1.7,
    pazymiai = [7, 7, 2, 3, 9, 8, 10, 9],
    grupe = 'IFM-3/4'
)

for pazymys in studentas['pazymiai']:
    if pazymys > 5:
        print(f'pazymys {pazymys} yra teigiamas')
    else:
        print(f'pazymys {pazymys} yra neigiamas')