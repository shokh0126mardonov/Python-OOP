class User:
    def __init__(self,username,email,is_activate):
        self.username = username
        self.email = email
        self.is_activate = is_activate
        
    def tanishtir(self):
        return f"username:{self.username} , email:{self.email} , activate:{self.is_activate}"
    

user1 = User("Shohjahon Mardonov","smardonov203@gmail.com",True)
user2 = User("Qalandarov Bexruzbek" , "qalandarov2005@gmail.com" , True)

print(user1.tanishtir())