skaiciai = [8, 5, 7, 4, 2, 3]

lyginiu_suma = 0
nelyginiu_suma = 0

for skaicius in skaiciai:
    if skaicius % 2 == 0:
        lyginiu_suma += skaicius
    else:
        nelyginiu_suma += skaicius

print('skaiciai:', skaiciai)
print('lyginiu suma:', lyginiu_suma)
print('nelyginiu suma:', nelyginiu_suma)