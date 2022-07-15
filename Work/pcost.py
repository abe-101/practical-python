# pcost.py
#
# Exercise 1.27

total_cost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        _, shares, price = line.split(',')
        total_cost += int(shares) * float(price)

print(f'Total cost {total_cost}')


