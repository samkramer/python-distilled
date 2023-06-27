# 6.4 Using Generators in Practice

# This implementation builds an internal stack of iterators. It is not subject
# to Python’s recursion limit because it’s putting data on an internal list 
# as opposed to building frames on the internal interpreter stack
def flatten(items):
    stack = [ iter(items) ]
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()

if __name__ == '__main__':   
    lst = [1, 2, [3, [4, 5], 6, 7], 8]
    print(f"Original list: {lst}")
    
    lst = list(flatten(lst))
    print(f"Flattened list: {lst}")