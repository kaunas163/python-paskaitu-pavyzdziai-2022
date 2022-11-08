import random

lyginiu_suma = 0
lyginiu_kiekis = 0

while lyginiu_kiekis < 5:
    skaicius = random.randint(1, 10)
    if skaicius % 2 == 0:
        print(skaicius, 'lyginis')
        lyginiu_kiekis += 1
        lyginiu_suma += skaicius
    else:
        print(skaicius)

print('rasta lyginiu suma:', lyginiu_suma)
