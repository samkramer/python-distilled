# 9.15.10 io Module
# https://docs.python.org/3/library/io.html
import io

# Function that expects a file
def greeting(file):
    file.write('Hello\n')
    file.write('World\n')
    
# Call the greeting function using a real file
def write(filename):
    with open(filename, 'w') as file:
        greeting(file)
    
# Call the greeting function with a "fake" file
def write_debug():
    file = io.StringIO()
    greeting(file)
    # Get the resulting output
    output = file.getvalue()
    print(output)
    
def read_debug(content):
    file = io.StringIO(content)
    while (line := file.readline()):
        print(line, end='')

if __name__ == "__main__":
    # write('out.txt')
    write_debug()
    read_debug('First line\nSecond line\n')