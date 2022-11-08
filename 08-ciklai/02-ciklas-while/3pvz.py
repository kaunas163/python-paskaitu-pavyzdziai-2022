prekiu_kiekis = 24

while prekiu_kiekis > 0:
    print(f'turimas prekiu kiekis: {prekiu_kiekis}')
    nupirkta = int( input('Kiek norite nupirkti? ') )
    print(f'nupirkote: {nupirkta} \n')
    prekiu_kiekis -= nupirkta
