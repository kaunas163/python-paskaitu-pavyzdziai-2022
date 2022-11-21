knyga = {
    'autorius': 'Jey k rauling',
    'pavadinimas': 'toks ir anoks pasaulis',
    'puslapiai': 245,
    'kaina': 14.99,
    'ar_prekyboje': True,
}

print(knyga['autorius'])
print(knyga.get('autorius'))

print(knyga['puslapiai'])
print(knyga.get('puslapiai'))