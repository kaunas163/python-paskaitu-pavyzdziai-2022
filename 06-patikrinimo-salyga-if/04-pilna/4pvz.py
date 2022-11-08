failas = 'uzrasai/2022-10-14.txt'

if failas == None:
    print('prasome nurodyti faila')
elif failas.endswith('.txt'):
    print('failo nuskaitymas...')
else:
    print('nurodytas netinkamo formato failas')
