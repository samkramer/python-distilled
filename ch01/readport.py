# Section 1.17 - Modules
# Reads a file of 'NAME,SHARES,PRICE' data entries

import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                holding = (name, shares, price)
                portfolio.append(holding)
            except ValueError as err:
                print(f"[ERROR] Invalid row: {row}")
                print(f"[ERROR] Reason: {err}")
    return portfolio


def main():
    portfolio = read_portfolio('data/portfolio.csv')
    for name, shares, price in portfolio:
        print(f"{name:>10s} {shares:10d} {price:10.2f}")

if __name__ == '__main__':
    main()