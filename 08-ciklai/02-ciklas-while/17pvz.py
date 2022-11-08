pazymiu_suma = 0
pazymiu_kiekis = 0

pazymys = -1

print('Iveskite tiek pazymiu kiek norite (atskiriant enter)')
print('Norint baigti irasykite 0')

while pazymys != 0:
    pazymys = int(input('Iveskite pazymi: '))
    if pazymys != 0:
        pazymiu_suma += pazymys
        pazymiu_kiekis += 1

vidurkis = round(pazymiu_suma / pazymiu_kiekis, 1)
print('Suvestu pazymiu vidurkis:', vidurkis)
