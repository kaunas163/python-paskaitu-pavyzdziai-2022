from csv import DictReader

with open('./studentai.csv', encoding='utf8') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row)