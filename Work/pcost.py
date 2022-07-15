# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", row)
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)


