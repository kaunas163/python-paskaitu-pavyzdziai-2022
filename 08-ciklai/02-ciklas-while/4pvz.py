prekiu_kiekis = 24

while prekiu_kiekis > 0:
    print(f'turimas prekiu kiekis: {prekiu_kiekis}')
    pirkimo_kiekis = int( input('Kiek norite nupirkti? ') )
    if pirkimo_kiekis > prekiu_kiekis:
        pirkimo_kiekis = prekiu_kiekis
    print(f'nupirkote: {pirkimo_kiekis} \n')
    prekiu_kiekis -= pirkimo_kiekis
