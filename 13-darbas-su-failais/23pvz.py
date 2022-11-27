with open('./rasymui5.txt', 'w') as failas:
    failas.write('labas krabas\n')

with open('./rasymui5.txt', 'a') as failas:
    failas.write('daugiau teksto\n')
    failas.write('failo papildymas')

with open('./rasymui5.txt', 'r+') as failas:
    failas.write('ar atsiras failo virsuje?\n')