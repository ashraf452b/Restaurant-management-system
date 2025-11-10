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
        self.myemployes=[]


    def add_emp(self,restaurant,emp):
        restaurant.add_emp(emp)


    def __repr__(self):
        return f"{self.name} {self.phone} {self.address} {self.email}"
    

class Menu:
    def __init(self):
        self.items=[]
        self.menu=Fooditem()


    def add_item(self,name):
        self.items.append(name)

    def find_item(self,name):
        for item in self.items:
            if item.lower()==name.lower():
                return item
        return None
    
    def remove_item(self,name):
        item=self.find_item(name)
        if item != None:
            self.items.remove(name)
        else:
            print(f'This item not found')
    
    def show_menu(self):
        print(f"name\tprice\tquantity")
        for i in self.items:
            print(f'{i.name}\t{i.quantity}\t{i.price}')
            

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]

    def add_emp(self,emp):
        self.employees.append(emp)
        print(f"{emp.name} Added!!")

    def view_emp(self):
        for emp in self.myemployes:
            print(emp.name,emp.phone,emp.address,emp.email,emp.designation,emp.salary,emp.age)


class Fooditem:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price

