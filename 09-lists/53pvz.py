skaiciai = [78, 47, 24, 36, 24, 14, 25, 98, 73]

for sk in skaiciai:
    isvedimas = f'skaicius {sk} yra '
    if sk % 2 == 0:
        isvedimas += 'lyginis'
    else:
        isvedimas += 'nelyginis'
    print(isvedimas)