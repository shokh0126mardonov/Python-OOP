class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        return
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Mablag' yetarli emas!")
        return
    
    def chiqarish(self):
        print(self)
    
    
    def __str__(self):
        return f"Owner: {self.owner}\nBalans: {self.balance} so'm"

    
   

user1 = BankAccount("Shohjahon",5_000)
     
print("1.Deposit")
print("2.Withdraw")

tanlov = int(input("tanlang : "))

if tanlov == 1:
    deposit = float(input(">>> "))
    user1.deposit(deposit)
    user1.chiqarish()
    
elif tanlov == 2:
    withdraw = float(input(">>> "))
    user1.withdraw(withdraw)
    user1.chiqarish()
