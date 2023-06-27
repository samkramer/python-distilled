# 9.11 Generating Output

def countdown(n):
    while n > 0:
        yield f"T-minus {n}"
        n -= 1
    yield "Kaboom!"
    
if __name__ == "__main__":
    lines = countdown(5)
    for line in lines:
        print(line)