# Chapter 4.14 Iteration Protocol

class FRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        
    # Use generator function involving yield
    def __iter__(self):
        x = self.start
        while x < self.stop:
            xr = round(x, 1)
            yield xr
            x += self.step

if __name__ == '__main__':
    nums = FRange(0.0, 1.0, 0.1)
    for n in nums:
        print(n)