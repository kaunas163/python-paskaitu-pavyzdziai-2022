def didziausio_paieska(skaiciu_masyvas):
    max = skaiciu_masyvas[0]

    for skaicius in skaiciu_masyvas:
        if skaicius > max:
            max = skaicius

    print('didziausias rastas skaicius:', max)


skaiciai1 = [7, 8, 99, 14, 557, 21, 23]
skaiciai2 = [9, 7, 4, 2, 3, 6, 8, 10, 21, 5]

print('skaiciai1:', skaiciai1)
didziausio_paieska(skaiciai1)

print('skaiciai2:',skaiciai2)
didziausio_paieska(skaiciai2)