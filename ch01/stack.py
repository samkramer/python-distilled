
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
        
    def pop(self):
        return self._items.pop()
    
    def __repr__(self):
        return f"<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>"
    
    def __len__(self):
        return len(self._items)
    

class NumericStack(Stack):
    def push(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Expected int or float')
        super().push(item)
    
if __name__ == '__main__':
    s = Stack()
    s.push('Dave')
    s.push('Brian')
    s.push('Albert')
    
    while len(s) > 0:
        item = s.pop()
        print(item)
        
    print()
        
    ns = NumericStack()
    ns.push(3)
    ns.push(2)
    ns.push(1)
    
    while len(ns) > 0:
        item = ns.pop()
        print(item)