studentai = [
    dict( vardas = 'Jonas', pazymiai = [8, 7, 8, 9, 6, 8] ),
    dict( vardas = 'Tomas', pazymiai = [10, 10, 9, 10, 9, 10] ),
    dict( vardas = 'Ugne', pazymiai = [9, 10, 9, 8] ),
]

didz_vidurk_stud = studentai[0]
didz_vidurkis = 0

for studentas in studentai:
    # pazymiu sumos paieska
    suma = 0
    for pazymys in studentas['pazymiai']:
        suma += pazymys
    
    # pazymiu vidurkio skaiciavimas
    vidurkis = round(suma / len(studentas['pazymiai']))

    # patikrinimas ar sitas vidurkis didesnis uz
    # iki dabar zinoma didziausia vidurki
    if vidurkis > didz_vidurkis:
        didz_vidurk_stud = studentas
        didz_vidurkis = vidurkis

print('studentas su didziausiu vidurkiu:')
print(didz_vidurk_stud)