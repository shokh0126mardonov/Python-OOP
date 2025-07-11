class BancAccount:
    def __init__(self,owner: str,balance = 0):
        self.owner = owner
        self.balance = balance
        
    def show_balance(self):
        print(self.balance)
    
    def get_balance(self):
        return self.balance
        
accounts: list[BancAccount] = [
    BancAccount("Shohjahon",100),
    BancAccount("Ali",99),
    BancAccount("Vali",98),
    BancAccount("Jon",97),
    BancAccount("Bob",96)
]

s = 0
for account in accounts:
    s += account.get_balance()
    
print(s)    