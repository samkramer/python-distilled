# 6.1 Generators and yiled

def countdown(n):
    print(f"Counting down from {n}")
    while n > 0:
        yield n
        n -= 1
        
if __name__ == '__main__':
    for x in countdown(5):
        print(f"T-minus {x}")