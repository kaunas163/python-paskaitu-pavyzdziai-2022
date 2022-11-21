studentas = {
    'vardas': 'Petras',
    'kursas': 2
}

kopija = studentas.copy()

studentas['vardas'] = 'Tomas'
kopija['kursas'] = 3

print('studentas', studentas)
print('kopija', kopija)