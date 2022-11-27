from csv import reader

with open('./studentai.csv', encoding='utf8') as failas:
    csv_reader = reader(failas)
    duomenys = list(csv_reader) # gaunam viska iskart
    print(duomenys)