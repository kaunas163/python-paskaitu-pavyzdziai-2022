studentai = [
    dict( vardas = 'Jonas', pazymiai = [8, 7, 8, 9, 6, 8] ),
    dict( vardas = 'Tomas', pazymiai = [10, 10, 9, 10, 9, 10] ),
    dict( vardas = 'Ugne', pazymiai = [9, 10, 9, 8] ),
]

for studentas in studentai:
    print('studentas(-e):', studentas['vardas'])
    suma = sum(studentas['pazymiai'])
    pazymiu_kiekis = len(studentas['pazymiai'])
    vidurkis = round(suma / pazymiu_kiekis)
    print('jos/jo pazymiu vidurkis:', vidurkis)
    print()