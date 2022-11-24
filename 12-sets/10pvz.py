miestai = ['Kaunas', 'Vilnius', 'Kaunas', 'Klaipeda', 'Panevezys', 'Siauliai', 'Vilnius']

print('visi miestai:', miestai, '\n')

unikalus_miestai = set(miestai)
unikalus_miestai_sarase1 = list(unikalus_miestai)
print('sarase1:', unikalus_miestai_sarase1, '\n')

unikalus_miestai_sarase2 = list(set(miestai))
print('sarase2:', unikalus_miestai_sarase2)