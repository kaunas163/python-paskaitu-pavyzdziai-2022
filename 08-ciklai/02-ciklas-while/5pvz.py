import random

while True:
    skaicius = random.randint(1, 100)
    print(skaicius)

    if skaicius % 7 == 0 and skaicius % 2 == 0:
        print(f'skaicius {skaicius} dalinasi is 7 ir is 2')
        break
