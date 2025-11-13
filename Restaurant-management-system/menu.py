class Menu:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)
    
    def find_item(self,item):
        for i in self.items:
            if i.name.lower()== item.lower():
                return i
        return None
    
    def remove_item(self,item):
        found=self.find_item(item)
        if found:
            self.items.remove(found)
        else:
            print(f"This item Not Found")
    
    def view_item(self):
        print('*******Menu**********')
        print('Naame\tPrice\tQuantity')
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
    
