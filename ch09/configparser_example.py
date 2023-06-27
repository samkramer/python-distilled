# 9.15.4 configparser Module
# https://docs.python.org/3/library/configparser.html

import configparser

# Create a config parser and read a file
cfg = configparser.ConfigParser()
cfg.read('data/config.ini')

# Extract values
s1n1 = cfg.get('section1', 'name1')
print(f"Value of [section1::name1] using get: {s1n1}")

# Alternate syntax of above:
s1n1_alt = cfg['section1']['name1']
print(f"Value of [section1::name1] using indexing: {s1n1_alt}")

s2n2 = cfg.get('section2', 'name2')
print(f"Value of [section2::name2] using get: {s2n2}")