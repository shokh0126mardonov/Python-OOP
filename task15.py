class Product:
    def __init__(self,name: str,price: float,in_stock:bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

    
product1 = Product("Noutbuk", 450.00, True)
product2 = Product("Sichqoncha", 25.50, True)
product3 = Product("Monitor", 150.00, False)
product4 = Product("Klaviatura", 30.00, True)
product5 = Product("Printer", 200.00, False)

products = [product1,product2,product3,product4,product5]

result = filter(lambda product: product.in_stock == True,products)

s = 0
for i in result:
    s += i.price
    
print(s)
