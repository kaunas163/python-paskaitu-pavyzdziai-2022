pirmo_stud_paz = [8, 7, 9, 8, 7, 9, 10, 9]
antro_stud_paz = [9, 9, 10, 8, 7, 6, 9]

pirmo_stud_vidurkis = round(sum(pirmo_stud_paz) / len(pirmo_stud_paz), 2)
antro_stud_vidurkis = round(sum(antro_stud_paz) / len(antro_stud_paz), 2)

print('PIRMAS STUDENTAS')
print('pazymiai:', pirmo_stud_paz)
print('vidurkis:', pirmo_stud_vidurkis)

print('ANTRAS STUDENTAS')
print('pazymiai:', antro_stud_paz)
print('vidurkis:', antro_stud_vidurkis)

print()

if pirmo_stud_vidurkis > antro_stud_vidurkis:
    print('pirmo studento vidurkis didesnis')
    skirtumas = round(pirmo_stud_vidurkis - antro_stud_vidurkis, 2)
    print('skirtumas tarp vidurkiu:', skirtumas)
elif antro_stud_vidurkis > pirmo_stud_vidurkis:
    print('antro studento vidurkis didesnis')
    skirtumas = round(antro_stud_vidurkis - pirmo_stud_vidurkis, 2)
    print('skirtumas tarp vidurkiu:', skirtumas)
else:
    print('abieju studentu vidurkiai vienodi')
