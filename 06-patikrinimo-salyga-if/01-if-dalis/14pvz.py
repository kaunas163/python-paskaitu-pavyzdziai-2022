# ternary operator / inline if

# [on_true] if [expression] else [on_false]

# jeigu klientas turi daugiau nei 100 tasku,
# jis yra 'gold' klientas, kitu atveju,
# jis yra 'silver' klientas

taskai = 110
tipas = 'gold' if taskai > 100 else 'silver'

print(tipas)
