# 7.8 Avoiding Inheritance via Composition

import array

class Stack:
    def __init__(self, *, container=None):
        if container is None:
            container = list()
        self._items = container
    
    def push(self, item):
        self._items.append(item)
        
    def pop(self):
        return self._items.pop()
    
    def __len__(self):
        return len(self._items)
    
if __name__ == '__main__':
    # Used typed array as container
    s = Stack(container=array.array('i'))
    s.push(42)
    s.push(23)
    
    # TypeError: 'str' object cannot be interpreted as an integer
    # s.push('my string')
    
    while (len(s) > 0):
        print(s.pop())