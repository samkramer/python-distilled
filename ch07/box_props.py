# 7.17 Properties

class Box(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
if __name__ == '__main__':
    b = Box(4, 5)
    print(f"area = {b.area}")
    print(f"perimeter = {b.perimeter}")
    
    # AttributeError: can't set attribute 'area'
    # b.area = 5