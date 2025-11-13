from abc import ABC
from orders import Order
class User(ABC):
    def __init__(self,name,phone,address,email):
        self.name=name
        self.phone=phone
        self.address=address
        self.email=email

class Employee(User):
    def __init__(self,name,phone,address,email,designation,salary,age):
        super().__init__(name,phone,address,email)
        self.designation=designation
        self.salary=salary
        self.age=age

class Admin(User):
    def __init__(self,name,phone,address,email):
        super().__init__(name,phone,address,email)
        
    
    def add_emp(self,restaurant,employee):
        restaurant.add_emp(employee)

    def view_emp(self,restaurant):
        restaurant.view_emp()
    
    def add_item(self,restaurant,item):
        restaurant.menu.add_item(item)

    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)

    def show_menu(self,restaurant):
        restaurant.menu.view_item()

class Customer(User):
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
        self.cart=Order()

    def add_cart(self,restaurant,item,quantity):
        self.found= restaurant.menu.find_item(item)
        if self.found:
            if quantity > self.found.quantity:
                print('Item Quantity Exceed')
            else:
                self.cart.add_item(self.found,quantity) 
                print('Item Added')
        else:
            print(f'{item} Not Found in this Restaurant')
             
    def  show_menu(self,restaurant):
        restaurant.menu.view_item()
    
    def view_cart(self):
        print(f"*******Your Cart*******")
        print(f'Item\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
            print(f'Total price : {self.cart.total_price}')

    def pay_bill(self):
        print('1. Cash Payment')
        print('2. Card Payment')
        print('3. Bkash Payment')
        while True:
            payment=int(input('Select Your Payment method '))
            if payment==1:
                print(f'Total {self.cart.total_price} paid succesfully via Cash')
            elif payment==2:
                print(f'Total {self.cart.total_price} paid succesfully via Card')
            elif payment==3:
                print(f'Total {self.cart.total_price} paid succesfully via Bkash')
            else:
                print('Invalid option Select Correct Method')
            if payment==1 or payment==2 or payment==3:
                break
            
        for item, quantity in self.cart.items.items():
            item.quantity -= quantity
        self.cart.clear_cart()

