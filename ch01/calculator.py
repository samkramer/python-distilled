import stack

class Calculator:
    def __init__(self):
        self._stack = stack.NumericStack()
    
    def push(self, item):
        self._stack.push(item)
        
    def pop(self):
        return self._stack.pop()
    
    def add(self):
        self.push(self.pop() + self.pop())
        
    def mul(self):
        self.push(self.pop() * self.pop())
        
    def sub(self):
        right = self.pop()
        self.push(self.pop() - right)
        
    def div(self):
        right = self.pop()
        self.push(self.pop() / right)

if __name__ == '__main__':
    calc = Calculator()
    calc.push(2)
    calc.push(3)
    calc.push(4)
    calc.mul()
    calc.add()
    final = calc.pop()
    print(final) # Expected: 14