with open('./rasymui6.txt', 'w') as file:
    file.write('I WAS HERE FIRST')

with open('./rasymui6.txt', 'r+') as file:
    file.write(':)')
    file.seek(10)
    file.write(':(')