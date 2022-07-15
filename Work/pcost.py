# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            try:
                _, shares, price = line.split(',')
                total_cost += int(shares) * float(price)
            except ValueError:
                print("Couldn't parse", line)
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)


