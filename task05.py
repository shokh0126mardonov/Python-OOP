class Product:
    def __init__(self,name: str,price: float,category: str,is_stock: bool):
        self.name = name
        self.price = price
        self.category = category
        self.is_stock = is_stock

product1 = Product("kabel",5999.99,"elektronika",True)
product2 = Product("Noutbuuk",9999999.99,"Texnika",False)

print(f"name : {product1.name} price : {product1.price}")
print(f"name : {product2.name} price : {product2.price}")