class Temperature:
    def __init__(self , temp1):
        self.temp1 = temp1
    def convert(self):
        K = self.temp1 + 273.5
        F = (self.temp1* 9/5) + 32
        print(f"{self.temp1} is Equal to {K} K")
        print(f"{self.temp1} is Equal to {F} F")

celsius = float(input("Enter Temperature in Celsius: "))
userTemp = Temperature(celsius)
userTemp.convert()


# Carts Total bill code 

class Products:
    def __init__(self , name , price):
        self.name = name 
        self.price = price
class CartItems:
    def __init__(self , product ,quantity):
        self.product = product
        self.quantity = quantity
    def item_total(self):
        return self.product.price * self.quantity
    
product1 = Products("Horse" ,3000)
product2 = Products("Swords" , 1500)
product3 = Products("Bow" , 10000)

cart1 = CartItems(product1 , 1)
cart2 = CartItems(product2 , 1)
cart3 = CartItems(product3 , 1) 

Total_Bill = cart1.item_total() + cart2.item_total() + cart3.item_total()
print("Total Bill = " , Total_Bill)
