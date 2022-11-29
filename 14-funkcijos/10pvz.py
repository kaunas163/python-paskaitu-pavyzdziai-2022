from random import randint

def skaiciuoti_suma(a, b):
    suma = a + b
    print(f'{a} + {b} = {suma}')

skaiciuoti_suma(6, 5)
skaiciuoti_suma(4, 9)

atsitiktinis1 = randint(1, 10)
atsitiktinis2 = randint(1, 10)

skaiciuoti_suma(atsitiktinis1, atsitiktinis2)