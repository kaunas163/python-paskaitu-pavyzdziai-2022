skaiciai = [8, 7, 9, 6, 5, 8, 4]

didziausias = skaiciai[0]

for sk in skaiciai:
    if sk > didziausias:
        didziausias = sk

print('didziausias skaicius:', didziausias)