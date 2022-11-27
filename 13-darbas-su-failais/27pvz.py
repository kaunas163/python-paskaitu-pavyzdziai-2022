from csv import reader

with open('./studentai.csv', encoding='utf8') as failas:
    csv_reader = reader(failas)
    next(csv_reader) # praleidziam pirma eilute
    for eilute in csv_reader:
        print(eilute)