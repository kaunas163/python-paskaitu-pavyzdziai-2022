from csv import DictReader

with open('./studentai.csv', encoding='utf8') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(f"Studentas(-e) {row['Vardas']} {row['Pavardė']} mokosi {row['Mokykla']}")