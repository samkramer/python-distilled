import inspect

# Traditional way to define repr
class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"{type(self).__name__}({self.x!r}, {self.y!r})"
    

def with_repr(cls):
    args = list(inspect.signature(cls).parameters)
    argvals = ', '.join('{self.%s!r}' % arg for arg in args)
    code = 'def __repr__(self):\n'
    code += f' return f"{cls.__name__}({argvals})"\n'
    locs = { }
    exec(code, locs)
    cls.__repr__ = locs['__repr__']
    return cls

# Use class decorator to generate repr
@with_repr
class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
if __name__ == '__main__': 
    pt1 = Point1(3, 4)
    print(repr(pt1))
    
    pt2 = Point2(3, 4)
    print(repr(pt2))