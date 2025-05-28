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

    
    
    print(f"\n1.- Laptop: $15,000")
    print(f"\n2.- Smartphone: $30,000")
    print(f"\n3.- Mouse: $500.00")

  
    #with more time, add number validation with "while" an except like main()
    product = int(input(f"\nSelect a product: "))
    price = 0
   
    if product == 1:
        product = "Laptop"
        price = 15000
    elif product == 2:
        product = "Smartphone"
        price = 30000
    elif product == 3:
        product = "Mouse"
        price = 500

    coupon = float(input(f"\nIntroduce % coupon: "))/100
    

    priceProduct = Product(product, price)
    
    print(f"El precio final de tu {product} es {priceProduct.get_discounted_price(coupon)}")

    input("\nPresiona Enter para regresar al menú...")
    clear_screen()
    main()

    #Buy applying 20% coupon
def Coupon20():

    
    
    print(f"\n1.- Laptop: $15,000")
    print(f"\n2.- Smartphone: $30,000")
    print(f"\n3.- Mouse: $500.00")

  

    product = int(input(f"\nSelect a product: "))
    price = 0
    #with more time, add number validation with "while" an except
    if product == 1:
        product = "Laptop"
        price = 15000
    elif product == 2:
        product = "Smartphone"
        price = 30000
    elif product == 3:
        product = "Mouse"
        price = 500


    Digital = DigitalProduct(product, price)

    
    print(f"Final price of your {product} applying a 20% discount is {Digital.get_discounted_price()}")
    input("\nPresiona Enter para regresar al menú...")
    clear_screen()
    main()


    

#with more time, find out why the program exit until second time to press "0"

def main():

    print(":*****************************************")
    print("*                                        *")
    print("*                                        *")
    print("*                 Welcome                *")
    print("*                                        *")
    print(":*****************************************")


    while True:
        print(f"\nChose an option:")

        print(f"\n1.- Buy product with a coupon")
        print(f"\n2.- Buy product online 20% disscount")
        print(f"\n0.- Press 0 to finish")
        try:
            
            option = int(input("Select an option: "))
        except ValueError:
            print("\nPlease enter a valid number.")
            continue 

        if option == 1:
            clear_screen() 
            BuyWithCoupon()

        if option == 2:
            clear_screen() 
            Coupon20()
        elif option == 0:
            clear_screen() 
            print("\nAdios..")
            break 
        else:
            print("\nInvalid option, try again.")    

if __name__ == "__main__":
    main()