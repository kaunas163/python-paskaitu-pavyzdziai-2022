from csv import reader, writer

with open('./cats.csv') as file:
    csv_reader = reader(file)
    cats = [ [s.upper() for s in row] for row in csv_reader ]
    print(cats)

with open('./cats-upper.csv', 'w', newline='') as file:
    csv_writer = writer(file)
    csv_writer.writerows(cats)