# 3.4.4 Chained Exceptions

class ApplicationError(Exception):
    pass

def do_something():
    x = int('N/A')  # raises ValueError
    print(x)

def spam():
    try:
        do_something()
    except Exception as e:
        raise ApplicationError('App failed') from e

if __name__ == '__main__':
    try:
        spam()
    except ApplicationError as e:
        print(f"Reason for exception: {e.__cause__}")
