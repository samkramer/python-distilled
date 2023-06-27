# Section 5.18 - Decorators
# @see trace.py for best practice

def trace(func):
    def call(*args, **kwargs):
        print('Calling: ', func.__name__)
        return func(*args, **kwargs)
    return call

@trace
def square(x):
    return x * x

if __name__ == '__main__':
    n = 3
    print(f"square({n}) = {square(n)}")
    
    # NOTE: must use @wraps for the following to work
    print(f"Function name: {square.__name__}")
    print(f"Function docstring: {square.__doc__}")
