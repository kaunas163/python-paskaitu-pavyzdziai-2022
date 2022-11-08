kartoti = 't'

while kartoti == 't':
    print("Iveskite du norimus skaicius (atskiriant enter):")
    pirmas = int( input() )
    antras = int( input() )
    print(f'{pirmas} + {antras} = {pirmas + antras}')
    kartoti = input('Ar norite kartoti? (t/n): ')

print('Pabaiga')
