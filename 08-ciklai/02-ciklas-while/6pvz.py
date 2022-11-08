import random

skaicius = 1

while skaicius % 7 != 0 or skaicius % 2 != 0:
    skaicius = random.randint(1, 100)
    print(skaicius)
