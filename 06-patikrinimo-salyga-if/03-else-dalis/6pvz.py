from random import randint

slaptas = randint(1, 10)

spejimas = int( input('Spekite skaiciu nuo 1 iki 10: ') )

if slaptas == spejimas:
    print('atspejote!')
else:
    print('deja, nepavyko :(((')
