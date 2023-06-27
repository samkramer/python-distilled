# 5.9 - Function Application and Parameter Passing

def func(x, y, z):
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")
    print()
    
if __name__ == '__main__':
    s = (1, 2, 3)
    func(*s)
    
    d = {'x' : 4, 'y' : 5, 'z' : 6}
    func(**d)
