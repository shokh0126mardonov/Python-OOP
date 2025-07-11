class BankAccount:
    def __init__(self,owner: str , balance: float):
        self.owner = owner
        self.balance = 00.0
        
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
        
    def show_balance(self):
         print(f"{self.owner} ning balansi {self.balance}")
    

account1 = BankAccount("Shohjahon",100)

account1.deposit(100)
account1.withdraw(500)
account1.show_balance()