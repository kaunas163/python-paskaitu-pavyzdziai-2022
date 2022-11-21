knygos = [
    { 'pavadinimas': 'apie saule', 'kaina': 14.00, 'autorius': 'Jonas Jonaitis' },
    { 'pavadinimas': 'miskininkas', 'kaina': 29.99, 'autorius': 'Petras Petrauskas' },
    { 'pavadinimas': 'mistika abc', 'kaina': 10.90, 'autorius': 'Gintare Gintaryte' },
    { 'pavadinimas': 'smegenu gidas', 'kaina': 25.49, 'autorius': 'Inga Ingute' },
    { 'pavadinimas': 'gyvuninkyste', 'kaina': 12.30, 'autorius': 'Gincius Ginciukas' },
]

kainu_suma = 0

print('visos knygos:')

for knyga in knygos:
    print(f"- {knyga['pavadinimas']} kaina {knyga['kaina']} eur")
    kainu_suma += knyga['kaina']

print('knygu kiekis:', len(knygos))
print('bendra suma:' , kainu_suma, 'eur')
print('bendra suma:' , round(kainu_suma, 2), 'eur')