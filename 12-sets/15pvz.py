miestai = {'Kaunas', 'Vilnius', 'Kaunas', 'Klaipeda', 'Panevezys', 'Siauliai', 'Vilnius'}

miestai.remove('Panevezys')
# miestai.remove('Birzai') # klaida

print(miestai)

miestai.discard('Birzai')
miestai.discard('Vilnius')

print(miestai)