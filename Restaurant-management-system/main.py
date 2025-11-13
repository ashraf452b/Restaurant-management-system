from food_item import *
from menu import *
from users import *
from restaurant import *
from orders import *





    # def add_cart(self,restaurant,item,quantity):      
    # def  show_menu(self,restaurant):
    #     restaurant.menu.view_item()
    # def view_cart(self):
       
    # def pay_bill(self): 
Restaurant_Name=Restaurant('Mamar Restaurant')
def customer_menu():
    name=str(input('Enter Your Name '))
    phone=input('Enter Your Phone ')
    email=input('Enter Your Email ')
    customer=Customer(name,phone,email)

    while True:
        print(f'Welcome {customer.name}!!')
        print('1. View Menu')
        print('2. Add item to cart')
        print('3. View item')
        print('4. PayBill')
        print('5. Exit')

        n=int(input('Enter  Your Choice'))
        
        if n==1:
            customer.show_menu(Restaurant_Name)
        elif n==2:
            item=input('Enter item Name ')
            quantity=int(input('Enter item Quantity '))
            customer.add_cart(Restaurant_Name,item,quantity)
        elif n==3:
            customer.view_cart()
        elif n==4:
            customer.pay_bill()
        elif n==5:
            print('Thank you for visiting Us')
            break
        else:
            print('Invalid Input!!')
            print('Try Again!!')


def admin_menu():
    name=str(input('Enter Your Name '))
    phone=input('Enter Your Phone ')
    address=input('Enter Your Address ')
    email=input('Enter Your Email ')
    admin=Admin(name,phone,address,email)

    while True:
        print(f'Welcome {admin.name}!!')
        print('1. Add item')
        print('2. Add Employee')
        print('3. View Employee')
        print('4. View item')
        print('5. Delete item')
        print('6. Exit')

        n=int(input('Enter Your Choice  '))
        if n==1:
            item_name=input('Enter item Name ')
            item_price=int(input('Enter item Price '))
            item_quantity=int(input('Enter item Quantity '))
            item=Fooditem(item_name,item_price,item_quantity)
            admin.add_item(Restaurant_Name,item)
        elif n==2:
            name,phone,address,email,designation,salary,age
            name=input('Enter Employee Name ')
            phone=input('Enter Employee Phone ')
            address=input('Enter Employee Address ')
            email=input('Enter Employee Email ')
            designation=input('Enter Employee Designation ')
            salary=int(input('Enter Salary '))
            age=int(input('Enter Age '))
            emp=Employee(name,phone,address,email,designation,salary,age)
            admin.add_emp(Restaurant_Name,emp)
        elif n==3:
            admin.view_emp(Restaurant_Name)
        elif n==4:
            admin.show_menu(Restaurant_Name)
        elif n==5:
            item=input('Enter item Name ')
            admin.remove_item(Restaurant_Name,item)
        elif n==6:
            break
        else:
            print('Invalid Input')
            print('Enter Correct Choice')




while True:
    print('1. Customer ')
    print('2. Admin')
    print('3. Exit')
    n=int(input('Enter Your Choice '))
    if n==1:
        customer_menu()
    elif n==2:
        admin_menu()
    elif n==3:
        break
    else:
        print('Invalid Option\nEnter Valid Choice ')
