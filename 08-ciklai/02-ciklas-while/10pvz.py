pradzia, pabaiga = 1, 100

skaicius = 0

while skaicius < pradzia or skaicius > pabaiga:
    skaicius = int( input('Iveskite skaiciu tarp [1-100]: ') )
    if skaicius < pradzia or skaicius > pabaiga:
        print('Blogas rezis!')

print('Pabaiga')
print('Ivestas skaicius:', skaicius)
