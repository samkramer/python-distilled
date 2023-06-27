# Section 1.17 - Modules

import readport as rp


def portfolio_cost(filename):
    """
    Compute total shares*price of a portfolio.
    """
    portfolio = rp.read_portfolio(filename)
    return sum((shares * price for _, shares, price in portfolio))

if __name__ == '__main__':
    data = "data/portfolio.csv" 
    cost = portfolio_cost(data)
    print(f"cost = ${cost:0.2f}")
