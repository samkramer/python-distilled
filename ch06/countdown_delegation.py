# 6.3 Generator Delegation
          
def countup(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1
        
def countdown(start):
    n = start
    while n >0:
        yield n
        n -= 1
        
# 'yield from' saves from having to drive iteration yourself
def up_and_down(n):
    yield from countup(n)
    yield from countdown(n)
    
# identical functionality to up_and_down
def up_and_down_2(n):
    for x in countup(n):
        yield x
    for x in countdown(n):
        yield x
        
def flatten(items):
    for i in items:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i


if __name__ == '__main__':
    for x in up_and_down(5):
        print(x, end=' ')
        
    print()
    
    for x in up_and_down_2(5):
        print(x, end=' ')
    print()
    
    lst = [1, 2, [3, [4, 5], 6, 7], 8]
    print(f"Original list: {lst}")
    
    lst = list(flatten(lst))
    print(f"Flattened list: {lst}")