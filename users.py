from abc import ABC

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
    def __init__(self,name,phone,address,email):
        super().__init__(name,phone,address,email)
        self.cart=None

    def add_cart(self,restaurant,item):
        found= restaurant.menu.find_item(item)
        if found:
            pass
        else:
            print('{item} Not Found in this Restaurant')
            
    def  show_menu(self,restaurant):
        restaurant.menu.view_item()

        
class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()
    
    def add_emp(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} Added !!")
    
    def view_emp(self):
        print('****Employees List****')
        for emp in self.employees:
            print(f"{emp.name} {emp.address} {emp.phone} {emp.email} {emp.designation} {emp.salary} {emp.age}")


class Menu:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)
    
    def find_item(self,item):
        for i in self.items:
            if i.name.lower()== item.lower():
                return item
        return None
    def remove_item(self,item):
        found=self.find_item(item)
        if found:
            self.items.remove(item)
        else:
            print(f"This item Not Found")
    
    def view_item(self):
        print('*******Menu**********')
        print('Naame\tPrice\tQuantity')
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
    

class Fooditem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity


res=Restaurant('Visca barca')
emp1=Employee('ashraf',123321,'dhaka','mail@hihii','chef',1200,18)
ad=Admin('ashraf',1232321,'dhaka','mail@email')
item=Fooditem('Pizza',15,100)
mn=Menu()
mn.add_item(item)
mn.view_item()
# ad.add_emp(res,emp1)
# ad.view_emp(res)


    