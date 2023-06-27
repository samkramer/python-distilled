# Section 5.18 - Decorators
from functools import wraps

def trace(func):
    @wraps(func)
    def call(*args, **kwargs):
        print('Calling: ', func.__name__)
        return func(*args, **kwargs)
    return call

@trace
def square(x):
    """
    Parameters
    ----------
    x : int
        argument to be squared

    Returns
    -------
    int
        square of argument
    """
    return x * x

if __name__ == '__main__':
    n = 3
    print(f"square({n}) = {square(n)}")
    
    print(f"Function name: {square.__name__}")
    print(f"Function docstring: {square.__doc__}")
