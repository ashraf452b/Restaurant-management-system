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
    employees=[]
    def __init__(self,name,phone,address,email):
        super().__init__(name,phone,address,email)
        
    
    def add_emp(self,restaurant,employee):
        restaurant.add_emp(employee)

    def view_emp(self,restaurant):
        restaurant.view_emp()
        
        
class Restaurant:
    employees=[]
    def __init__(self,name):
        self.name=name
    
    def add_emp(self,employee):
        self.employees.append(employee)
        print(f"{employee.name} Added !!")
    
    def view_emp(self):
        print('****Employees List****')
        for emp in self.employees:
            print(f"{emp.name} {emp.address} {emp.phone} {emp.email} {emp.designation} {emp.salary} {emp.age}")


res=Restaurant('Visca barca')
    
emp1=Employee('ashraf',123321,'dhaka','mail@hihii','chef',1200,18)

ad=Admin('ashraf',1232321,'dhaka','mail@email')
ad.add_emp(res,emp1)
ad.view_emp(res)


    