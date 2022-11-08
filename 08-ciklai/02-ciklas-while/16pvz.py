pazymiu_suma = 0
pazymiu_kiekis = 0

dar_ivesti = 't'

while dar_ivesti == 't':
    pazymys = int(input('Iveskite pazymi: '))
    pazymiu_suma += pazymys
    pazymiu_kiekis += 1
    dar_ivesti = input('Ar dar norite ivesti? (t/n) ')

vidurkis = round(pazymiu_suma / pazymiu_kiekis, 1)
print('Suvestu pazymiu vidurkis:', vidurkis)
