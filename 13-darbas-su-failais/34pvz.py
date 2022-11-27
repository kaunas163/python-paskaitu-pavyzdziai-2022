from csv import writer

with open('./fighters.csv', 'w', newline='') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Character', 'Move'])
    csv_writer.writerow(['Ryu', 'Hadouken'])