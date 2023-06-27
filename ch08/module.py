## 8.1 Modules and the import statement

## Type the following in python console:
# >>> import module
# >>> module.a          --> 37
# >>> module.func()     --> func says that a is 37
# >>> s = module.SomeClass()
# >>> s.method()        --> method says hi

# Global variable
a = 37

# Function
def func():
    print(f'func says that a is {a}')
    
# Class definition
class SomeClass:
    def method(self):
        print('method says hi')
        
# Isolated statement
print('loaded module')


