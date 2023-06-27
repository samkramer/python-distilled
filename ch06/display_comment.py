# 6.4 Using Generators in Practice

import pathlib
import re

# Display comment lines that contain word in python script
# Note: original version with multiple levels of nesting
# See: display_comment_2.py for better approach
def display_comment(filepath, word):
    for path in pathlib.Path(filepath).rglob('*.py'):
        if path.exists():
            with path.open('rt', encoding='latin-1') as file:
                for line in file:
                    m = re.match('.*(#.*)$', line)
                    if m:
                        comment = m.group(1)
                        if word in comment:
                            print(f"[{path.name}] {comment}")
                            
if __name__ == '__main__':
    target_dir = r"C:\temp\book_code\python\effectivepython\example_code"
    word = 'Verify'
    display_comment(target_dir, word)
    