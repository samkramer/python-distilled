# 6.2 Restartable Generators

class countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
        
if __name__ == '__main__':
    for x in countdown(5):
        print(f"T-minus {x}")