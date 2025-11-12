from menu import Menu
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
