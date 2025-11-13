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
        found= restaurant.menu.find_item(item)
        if found:
            if quantity > found.quantity:
                print('Item Quantity Exceed')
            else:
                found.quantity=quantity
                print('Item Added')
                self.cart.add_item(found)
        else:
            print('{item} Not Found in this Restaurant')
             
    def  show_menu(self,restaurant):
        restaurant.menu.view_item()
    
    def view_cart(self):
        print(f"*******Your Cart*******")
        print(f'Item\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
            print(f'Total price : {self.cart.total_price}')
    def pay_bill(self):
        print(f'Total {self.cart.total_price} paid succesfully')
        self.cart.clear()

