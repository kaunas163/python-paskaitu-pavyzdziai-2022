masinos = ['audi', 'bmw', 'volvo', 'mercedes', 'opel']
masinos[4] = 'bentley'

print(masinos)

kopija = masinos
print(kopija)

masinos[1] = 'NAUJAS'
print(masinos)
print(kopija)