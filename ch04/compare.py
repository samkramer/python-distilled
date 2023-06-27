def compare(a, b):
    print(f"a = {a}")
    print(f"b = {b}")
    
    if a is b:
        print('Same object')
        
    if a == b:
        print('Same value')
        
    if type(a) is type(b):
        print('Same type')
        
    print()
        
if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1, 2, 3]
    
    compare(a, a)
    compare(a, b)
    compare(a, [4, 5, 6])
    
    if (isinstance(a, list)):
        print('a is a list')