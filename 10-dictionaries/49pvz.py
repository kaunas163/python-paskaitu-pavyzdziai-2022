studentas = dict(
    vardas = 'Tomas',
    pavarde = 'Tomauskas',
    amzius = 23,
    ugis = 1.7,
    pazymiai = [7, 7, 2, 3, 9, 8, 10, 9],
    grupe = 'IFM-3/4'
)

kitas = {}

kitas.update(studentas)

print(studentas)
print(kitas)
print()

kitas['amzius'] = 24
kitas.update(studentas)

print(studentas)
print(kitas)