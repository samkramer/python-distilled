# Section 5.19 - Map, Filter, Reduce

import math
from functools import reduce

nums = [1, 2, 3, 4, 5]

# -- Using  reduce --

total = reduce(lambda x, y: x + y, nums)
print(f"total: {total}")

product = reduce(lambda x, y: x * y, nums)
print(f"product: {product}")

print()

# -- (preferred) Using built-ins --

total = sum(nums)
print(f"total: {total}")

product = math.prod(nums)
print(f"product: {product}")
