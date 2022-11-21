studentas = {
    'vardas': 'Petras',
    'pavarde': 'Petrauskas',
    'amzius': 22,
    'kur_mokosi': {
        'mokykla': 'KTU',
        'studiju_programa': 'Multimedijos technologijos',
        'kursas': 3
    },
    'pazymiai': [7, 8, 9, 6, 8, 5, 4]
}

print('studentas:', studentas)
print('duomenu tipas:', type(studentas))
print('vardas:', studentas['vardas'])
print('amzius:', studentas['amzius'])
print('kur mokosi:', studentas['kur_mokosi'])
print('kursas:', studentas['kur_mokosi']['kursas'])
print('pazymiai:', studentas['pazymiai'])
print('kazkuris pazymys:', studentas['pazymiai'][2])