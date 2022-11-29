def rodyti_informacija(vardas='Ieva', ar_lektorius=False):
    if vardas == 'Ieva' and ar_lektorius:
        return 'Sveika sugrizus Ieva'
    elif vardas == 'Ieva':
        return 'As galvojau tu lektore...'
    return f'Labas {vardas}'

print( rodyti_informacija() )
print( rodyti_informacija(ar_lektorius=True) )
print( rodyti_informacija('Ugnius') )