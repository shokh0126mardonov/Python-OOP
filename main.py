class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    def __str__(self):
        return f"{self.ism} {self.familiya}, {self.tyil}-yilda tug‘ilgan"
    
        
talaba1 = Talaba('Shohjahon','Mardonov',2006)
talaba2 = Talaba("Bexrux",'Qalandarov',2005)
print(talaba2)