import random

slaptas = random.randint(1, 10)
spejimas = None

while slaptas != spejimas:
    spejimas = int(input('Spekite skaiciu tarp 1 ir 10: '))
    if slaptas != spejimas:
        print('Deja nepavyko, bandykite dar karta')
    else:
        print('Laimejote!')
