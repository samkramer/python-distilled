# Reads input lines of the form 'NAME,SHARES,PRICE'.
# For example:
# SYM,123,456.78

import sys
from collections import Counter

data = "data/portfolio.csv"
# data = "data/portfolio_invalid.csv"

portfolio = []
with open(data, 'rt') as file:
    for line in file:
        line = line.strip()
        row = line.split(',')
        try:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            holding = (name, shares, price)
            portfolio.append(holding)
        except ValueError as err:
            print(f"[ERROR] Invalid row: {row}")
            print(f"[ERROR] Reason: {err}")
            sys.exit(1)

for entry in portfolio:
    print(entry)
    
print()

total_cost_1 = sum([int(row[1]) * float(row[2]) for row in portfolio])
print(f"Total cost #1: ${total_cost_1:0.2f}")

total_cost_2 = sum([shares * price for _, shares, price in portfolio])
print(f"Total cost #2: ${total_cost_2:0.2f}")

print()

total_shares_1 = { s[0] : 0 for s in portfolio }
for name, shares, _ in portfolio:
    total_shares_1[name] += shares
print(f"Total shares #1: {total_shares_1}")

total_shares_cnt = Counter()
for name, shares, _ in portfolio:
    total_shares_cnt[name] += shares
total_shares_2 = dict(total_shares_cnt)
print(f"Total shares #2: {total_shares_2}")
