failai = [
    'naujienos/pirma.txt',
    'naujienos/antra.txt',
    'naujienos/trecia.txt',
    'naujienos/ketvirta.txt',
    'naujienos/penkta.txt'
]

print('naujienu failai:', failai)
print('naujienu kiekis:', len(failai))
print()

dar_viena = 'naujienos/sesta.txt'
failai.append(dar_viena)

print('papildomai prideta naujiena:', dar_viena)
print('naujienu failai:', failai)
print('naujienu kiekis:', len(failai))