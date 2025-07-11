class Book:
    def __init__(self,title,author,is_read):
        self.title = title
        self.author = author
        self.is_read = is_read
        
    def mark_as_read(self):
        self.is_read = True
        
    def status(self):
        return self.is_read 
        
book1 = Book("Python dasturlash asoslari","Shohjahon")
book2 = Book("Sun'iy intellektga kirish", "Andrew Ng")
book3 = Book("Sifatli Kod", "Robert C. Martin")
book4 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev")
book5 = Book("Xamsa","Alisher Navoiy")

book2.mark_as_read()
book1.mark_as_read()

books = [book1,book2,book3,book4,book5]


for book in books:
    book.status()
    
print("O'qilganlar:")   
for book in books:
    if book.is_read:
        print("O'qilganlar:")
        
        