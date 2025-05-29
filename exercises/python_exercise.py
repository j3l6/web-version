# Product and DigitalProduct Exercise
#
# Instructions:
# 1. Implement a class `Product` with:
#    - Constructor: takes `name` (str) and `price` (float)
#    - Method: `get_discounted_price(discount_rate)` returns the price after applying the given discount rate (e.g., 0.2 for 20% off), rounded to 2 decimals
# 2. Implement a class `DigitalProduct` that inherits from `Product`:
#    - Overrides `get_discounted_price()` (no arguments) to always return the price with a fixed 20% discount, rounded to 2 decimals
#
# Write your solution in this file.

# Your code here:
import os
from typing import Any

#clear screen

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Parent class
class Product:

    def __init__(self, name : str, price : float) -> None:
        self.name = name
        self.price = price

    def get_discounted_price(self, discount_rate) -> float:
        finalprice = self.price - (self.price * discount_rate)
        return round(finalprice, 2)


#class from Product Class
class DigitalProduct(Product):

    def __init__(self, name=str, price=float) -> None:
        super().__init__(name, price)


    def get_discounted_price(self) -> float:

        get_discounted_price_overrided = super().get_discounted_price(.2)

        return get_discounted_price_overrided


#Buy appliyng manual coupon
def BuyWithCoupon():
    
    
    while True:
        
        print(":*****************************************")
        print("*                                        *")
        print("*                                        *")
        print("*               Buy Product              *")
        print("*                                        *")
        print(":*****************************************")
        print(f"\n1.- Laptop: $15,000")
        print(f"\n2.- Smartphone: $30,000")
        print(f"\n3.- Mouse: $500.00")
        
        try:
            product = int(input(f"\nSelect a product: "))
        except ValueError:
            clear_screen() 
            print("\nPlease enter a valid number.")
            continue
        
        price = 0
        
        if product == 1:
            product = "Laptop"
            price = 15000
            break
        elif product == 2:
            product = "Smartphone"
            price = 30000
            break
        elif product == 3:
            product = "Mouse"
            price = 500
            break
        else:
            clear_screen()
            print("\nPlease enter a valid number.")

    
    #add validation coupon < 0 or > 4
    
    coupon = float(input(f"\nIntroduce % coupon: "))/100
      
    priceProduct = Product(product, price)
    clear_screen()
    print(f"El precio final de tu {product} es {priceProduct.get_discounted_price(coupon)}")
    print("\nPlease enter a valid number.")
    input("\nPresiona Enter para regresar al menú...")
    clear_screen()
    return

    #Buy applying 20% coupon
def Coupon20():
    
    while True:
        
        print(":*****************************************")
        print("*                                        *")
        print("*                                        *")
        print("*               Coupon 20%               *")
        print("*                                        *")
        print(":*****************************************")
        print(f"\n1.- Laptop: $15,000")
        print(f"\n2.- Smartphone: $30,000")
        print(f"\n3.- Mouse: $500.00")
        
        try:
            product = int(input(f"\nSelect a product: "))
        except ValueError:
            clear_screen() 
            print("\nPlease enter a valid number.")
            continue 
        
    
        price = 0

        if product == 1:
            product = "Laptop"
            price = 15000
            break
        elif product == 2:
            product = "Smartphone"
            price = 30000
            break
        elif product == 3:
            product = "Mouse"
            price = 500
            break
        else:
            clear_screen()
            print("\nPlease enter a valid number.")
            
    Digital = DigitalProduct(product, price)
    clear_screen()
    print(f"Final price of your {product} applying a 20% discount is {Digital.get_discounted_price()}")
    input("\nPresiona Enter para regresar al menú...")
    clear_screen()
    return


    

#with more time, find out why the program exit until second time to press "0"

def main():

    
    while True:
        
        print(":*****************************************")
        print("*                                        *")
        print("*                                        *")
        print("*                 Welcome                *")
        print("*                                        *")
        print("******************************************")
        
        print(f"\nChose an option:")

        print(f"\n1.- Buy product with a coupon")
        print(f"\n2.- Buy product online 20% disscount")
        print(f"\n0.- Press 0 to finish")
        
        try:
            option = int(input("Select an option: "))
        except ValueError:
            clear_screen() 
            print("\nPlease enter a valid number.")
            clear_screen()  
            continue 
        
        print(option)
        
        if option == 0:
            clear_screen()
            print("\nAdios..")
            break
    

        elif option == 1:
            clear_screen()   
            BuyWithCoupon()
           

        elif option == 2:
            clear_screen()
            Coupon20()
        else:
            clear_screen()
            print("\nPlease enter a valid number.")
            
        
       
            

if __name__ == "__main__":
    main()