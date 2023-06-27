# 7.6 Operator Overloading and Protocols

class Account:    
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
    
class AccountPortfolio:
	def __init__(self):
		self.accounts = []
		
	def add_account(self, account):
		self.accounts.append(account)
		
	def total_funds(self):
		return sum(account.inquiry() for account in self.accounts)
		
	def __len__(self):
		return len(self.accounts)
		
	def __getitem__(self, index):
		return self.accounts[index]
		
	def __iter__(self):
		return iter(self.accounts)
    
    
if __name__ == '__main__':  
    guido = Account('Guido', 1000.00)
    eva = Account('Eva', 500.00)
    
    port = AccountPortfolio()
    port.add_account(guido)
    port.add_account(eva)
    
    print(f"Total balance of accounts: ${port.total_funds():0.2f}")
    print(f"Number of accounts: {len(port)}") # calls __len__
    
    print()
    
    # calls __iter__
    print("Accounts:")
    for account in port:
        print(f"  {account}")
        
    print()
        
    # Access individual account balance by index
    # calls __getitem__
    print(f"Second account balance: ${port[1].inquiry():0.2f}")
