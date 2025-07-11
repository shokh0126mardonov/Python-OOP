class Book:
    def __init__(self,title: str,author: str,is_read):
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
            
    def __str__(self):
        holat = "O'qilgan" if self.is_read else "O'qilmagan"
        return f"{self.author} ning {self.title} kitobi {holat}"
            
        
book1 = Book("Python dasturlash asoslari","Shohjahon",False)
book2 = Book("Sun'iy intellektga kirish", "Andrew Ng",False)
book3 = Book("Sifatli Kod", "Robert C. Martin", True)
book4 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev", True)

book1.status()
book1.mark_as_read()
print(book1)

book2.status()
book2.mark_as_read()
print(book2)

book3.status()
book3.mark_as_read()
print(book3)

book4.status()
book4.mark_as_read()
print(book4)