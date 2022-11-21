knygos = [
    dict(pavadinimas = 'apie saule', kaina = 14.00, autorius = 'Jonas Jonaitis'),
    dict(pavadinimas = 'miskininkas', kaina = 29.99, autorius = 'Petras Petrauskas'),
    dict(pavadinimas = 'mistika abc', kaina = 10.90, autorius = 'Gintare Gintaryte'),
    dict(pavadinimas = 'smegenu gidas', kaina = 25.49, autorius = 'Inga Ingute'),
    dict(pavadinimas = 'gyvuninkyste', kaina = 12.30, autorius = 'Gincius Ginciukas'),
]

for knyga in knygos:
    print(f"- {knyga['pavadinimas']} ({knyga['autorius']}) kaina {knyga['kaina']} €")