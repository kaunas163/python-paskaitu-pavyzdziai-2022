pradzia, pabaiga = 1, 100

skaicius = 0

while True:
    skaicius = int( input('Iveskite skaiciu tarp [1-100]: ') )
    if skaicius < pradzia or skaicius > pabaiga:
        print('Blogas rezis!')
    else:
        break

print('Pabaiga')
print('Ivestas skaicius:', skaicius)
