studentai = []

with open('./studentai.txt', encoding="utf8") as failas:
    for eilute in failas:
        eilute = eilute.rstrip('\n')
        isskaidyta = eilute.split(';')
        studentas = dict(
            vardas = isskaidyta[0],
            pavarde = isskaidyta[1],
            amzius = isskaidyta[2],
            mokykla = isskaidyta[3],
            vidurkis = isskaidyta[4]
        )
        studentai.append(studentas)

print(studentai)