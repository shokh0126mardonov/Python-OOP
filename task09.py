class User:
    def __init__(self, username, email, is_activate):
        self.username = username
        self.email = email
        self.is_activate = is_activate

    def activate(self):
        if not self.is_activate:
            self.is_activate = True 
            print(f"{self.username} faollashtirildi.")
        else:
            print(f"{self.username} allaqachon faollashtirilgan.")

    def deactivate(self):
        if self.is_activate:
            self.is_activate = False
            print(f"{self.username} faolsizlantirildi.")
        else:
            print(f"{self.username} allaqachon faol emas.")

    def __str__(self):
        holat = "faol" if self.is_activate else "faol emas"
        return f"Foydalanuvchi: {self.username}, Email: {self.email}, Holati: {holat}"



user1 = User("Shohjahon", "smardonov203@gmail.com", False)
user2 = User("Bexruz", "bexruz@gmail.com", True)

user1.activate()
user2.deactivate()
