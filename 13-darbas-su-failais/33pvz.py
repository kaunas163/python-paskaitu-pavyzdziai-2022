from csv import reader

with open('./studentai.csv', encoding='utf8') as file:
    csv_reader = reader(file, delimiter=',') # delimiter galima naudoti ir su paprastu reader
    for row in csv_reader:
        print(row)