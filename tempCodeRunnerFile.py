sales = [1200, 0, 1550, -100, 1800]
for amount in sales:
    if amount <= 0:  # skip zero or negative entries
        continue
    print(f"Processing sale: ${amount}")
