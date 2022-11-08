while True:
    print("Iveskite du norimus skaicius (atskiriant enter):")
    pirmas = int( input() )
    antras = int( input() )
    print(f'{pirmas} + {antras} = {pirmas + antras}')
    kartoti = input('Ar norite kartoti? (t/n): ')
    if kartoti != 't':
        print('Daugiau nebekartojama')
        break

print('Pabaiga')
