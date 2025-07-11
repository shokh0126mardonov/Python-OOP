class Product:
    def __init__(self,name:str,price: float,category: str):
        self.name = name
        self.price = price
        self.category = category
        
    def info(self):
        print(f"Mahsulot : {self.name} \nNarx : {self.price}")
        
    def mx(self):
        print(max(self.price))

Products:list[Product] = [
    Product("Noutbuk", 450.00, "Elektronika"),
    Product("Sichqoncha", 25.50, "Elektronika"),
    Product("Monitor", 150.00, "Elektronika"),
    Product("Klaviatura", 30.00, "Elektronika"),
    Product("Printer", 200.00, "Elektronika"),
    Product("Kalonka", 50.00, "Elektronika")
]

max_product = max(Products, key=lambda product: product.price)

max_product.info()