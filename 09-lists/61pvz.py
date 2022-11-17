skaiciai = [8, 7, 9, 6, 5, 8, 4]

didziausias = skaiciai[0]
didziausio_indeksas = 0

for i, skaicius in enumerate(skaiciai):
    if skaicius > didziausias:
        didziausias = skaicius
        didziausio_indeksas = i

print('didziausias skaicius:', didziausias)
print('didziausio indeksas:', didziausio_indeksas)