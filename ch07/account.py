# 7.2 The class statement

class Account:
    """
    A simple bank account
    """
    
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance
    
    def __repr__(self) -> str:
        return f"Account({self.owner!r}, {self.balance!r})"
    
    def deposit(self, amount: float) -> None:
        self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        self.balance -= amount
    
    def inquiry(self) -> float:
        return self.balance
    
if __name__ == '__main__':  
    a = Account('Guido', 1000.00)
    b = Account('Eva', 100.00)
    
    a.deposit(100.00)
    b.withdraw(50.00)
    
    print(repr(a))
    print(repr(b))
    
    func_name = 'deposit'
    if hasattr(b, func_name):
        func = getattr(b, func_name)
        func(250.00)
    else:
        print(f"[ERROR] Account class missing attribute: {func_name}")
    
    print(repr(b))
    