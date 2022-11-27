from csv import DictWriter

with open('./fighters-write.csv', 'w', newline='') as file:
    headers = ['Character', 'Move']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": 'Ryu',
        'Move': 'Hadouken'
    })