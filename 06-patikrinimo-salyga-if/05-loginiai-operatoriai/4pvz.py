pradzia = 1
pabaiga = 100

skaicius = int( input('Iveskite skaiciu: ') )

print()
print('reziai [', pradzia, '-', pabaiga, ']')
print('duotas skaicius:', skaicius)

if skaicius >= pradzia and skaicius <= pabaiga:
    print('patenka i rezius')
else:
    print('nepatenka i rezius')
