class Book:
    def __init__(self,title,author,is_read):
        self.title = title
        self.author = author
        self.is_read = is_read
        
    def status(self):
        if self.is_read:
            print("O'qilgan")
        else:
            print("O'qilmagan")
    
    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            print(f"{self.title} kitob o'qilgan deb belgilandi")
    
    def __str__(self):
        holat = "O'qilgan" if self.is_read else "O'qilmagan"
        return f"Muallifi {self.author} ning {self.title} kitobi {holat}"
    
book1 = Book("Python dasturlash asoslari","Shohjahon",False)
book2 = Book("Sun'iy intellektga kirish", "Andrew Ng",False)
book3 = Book("Sifatli Kod", "Robert C. Martin", False)
