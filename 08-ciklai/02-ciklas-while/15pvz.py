import random

slaptas = random.randint(1, 10)
spejimas = None

while slaptas != spejimas:
    spejimas = int(input('Spekite skaiciu tarp 1 ir 10: '))
    if slaptas > spejimas:
        print('Bandykite didesni')
    elif slaptas < spejimas:
        print('Bandykite mazesni')
    else:
        print('Atspejote!')
