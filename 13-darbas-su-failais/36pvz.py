from csv import reader, writer

with open('./cats.csv') as file_read:
    csv_reader = reader(file_read)
    with open('./cats2.csv', 'w', newline='') as file_write:
        csv_writer = writer(file_write)
        for cat in csv_reader:
            csv_writer.writerow(cat)