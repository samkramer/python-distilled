# 7.17 Properties

import string

class Account:
    def __init__(self, owner, balance):
        self.owner = owner  # assign to property setter!
        self._balance = balance
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, str):
            raise TypeError("[ERROR] Expected type 'str'")
        if not all(c in string.ascii_uppercase for c in value):
            raise ValueError("[ERROR] All characters must be uppercase")
        if len(value) > 10:
            raise ValueError("[ERROR] Must be 10 characters or less")
        self._owner = value
    
    def __repr__(self):
        return f'{type(self).__name__}({self.owner!r}, {self._balance!r})'
    
if __name__ == '__main__':
    a = Account('GUIDO', 1000.00)
    print(a)
    
    try:
        a.owner = "Eva"
        print(a)
    except (TypeError, ValueError) as e:
        print(e)
        
    try:
        a.owner = 100
        print(a)
    except (TypeError, ValueError) as e:
        print(e)
    
    try:
        a.owner = "RAMAKRISHNAN"
        print(a)
    except (TypeError, ValueError) as e:
        print(e)
        
    try:
        a.owner = "EVA"
        print(a)
    except (TypeError, ValueError) as e:
        print(e)
    
