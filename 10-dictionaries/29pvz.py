donations = dict(
    sam=25.0,
    lena=88.99,
    chuck=13.0,
    linus=99.5,
    stan=150.0,
    lisa=50.25,
    harrison=10.0
)

total_donations = 0

for donation_amount in donations.values():
    total_donations += donation_amount

print(total_donations)