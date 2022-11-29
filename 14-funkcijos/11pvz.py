from random import randint

def suma(a, b):
    print(f'{a} + {b} = {a + b}')

def skirtumas(a, b):
    print(f'{a} - {b} = {a - b}')

sk1 = randint(1, 10)
sk2 = randint(1, 10)

suma(sk1, sk2)
skirtumas(sk1, sk2)