studentai = [
    dict( vardas = 'Jonas', pazymiai = [8, 7, 8, 9, 6, 8] ),
    dict( vardas = 'Tomas', pazymiai = [10, 10, 9, 10, 9, 10] ),
    dict( vardas = 'Ugne', pazymiai = [9, 10, 9, 8] ),
]

for studentas in studentai:
    suma = sum(studentas['pazymiai'])
    studentas['vidurkis'] = round(suma / len(studentas['pazymiai']))
    
print(studentai)
print()

didz_vid_studentas = studentai[0]

for studentas in studentai:
    if studentas['vidurkis'] > didz_vid_studentas['vidurkis']:
        didz_vid_studentas = studentas

print('Studentas(-e) su didziausiu vidurkiu:')
print(didz_vid_studentas)