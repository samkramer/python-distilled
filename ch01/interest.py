# Section 1.3 - Primitives, Variables and Expressions
# Program uses variables and expressions to perform a compound-interest calculation

principal = 1000    # Initial amount
rate = 0.05         # Interest rate
num_years = 5       # Number of years
year = 1
while year <= num_years:
    principal = principal * (1 + rate)
    # '>3d' means a three-digit decimal number, right aligned
    # '0.2f' means a floating-point number with two decimal places of accuracy
    print(f'{year:>3d} {principal:0.2f}')
    year += 1
