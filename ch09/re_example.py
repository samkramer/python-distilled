# 9.15.16 re Module
import re

text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
print(f"original text: {text}")

# Find all occurrences of a date
dates = re.findall(r'\d+/\d+/\d+', text)
print(dates)    # ['3/27/2018', '3/28/2018']

# Replace all occurrences of a date with replacement text
text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(f"modified text: {text}") # 'Today is 2018-3-27. Tomorrow is 2018-3-28.'