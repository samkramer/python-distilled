# 7.23 Object Life Cycle and Memory Management

def open_resource():
    file = open("C:\\temp\\python-distilled\\README.md")
    # lines = file.readlines()
    # for line in lines:
    #     print(line)
    return file


class SomeClass:
    def __init__(self):
        self.resource = open_resource()
    
    def __del__(self):
        self.close()
    
    def close(self):
        print("[INFO] SomeClass::close()")
        self.resource.close()
        
    def __enter__(self):
        return self
    
    def __exit__(self, ty, val, tb):
        self.close()
        
        
if __name__ == '__main__':
    # Closed via __del__()
    s = SomeClass()
    del s
    
    # Explicit close
    s = SomeClass()
    s.close()
    
    # Closed at end of context block
    with SomeClass() as s:
        pass
