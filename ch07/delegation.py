# 7.26 Properties, Wrappers and Delegation
# Example of delegation

class A:
    def spam(self):
        print("A.spam")
    
    def grok(self):
        print("A.grok")
    
    def yow(self):
        print("A.yow")
    
class B:
    def __init__(self):
        self._a = A()
    
    # Redefines method from class A
    def grok(self):
        print("B.grok")
    
    # All other methods are delegated by forwarding attribute lookup
    def __getattr__(self, name):
        return getattr(self._a, name)
    
if __name__ == "__main__":
    b = B()
    b.spam()    # -> A.spam
    b.grok()    # -> B.grok (redefined method)
    b.yow()     # -> A.yow