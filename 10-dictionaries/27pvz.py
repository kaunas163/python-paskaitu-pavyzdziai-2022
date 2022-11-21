studentas = {
    'vardas': 'Tomas',
    'pavarde': 'Tomauskas',
    'amzius': 23,
    'ugis': 1.7,
    'pazymiai': [7, 7, 8, 7, 9, 8, 10, 9],
    'grupe': 'IFM-3/4'
}

paz_suma = 0

for paz in studentas['pazymiai']:
    paz_suma += paz

vidurkis = paz_suma / len(studentas['pazymiai'])
print('pazymiai', studentas['pazymiai'])
print('pazymiu vidurkis', vidurkis)