class Order:
    def __init__(self):
        self.items={}
        
    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
    
    def remove_item(self,item):
        if item in self.items:
            self.items.pop(item)
    @property
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())
    
    def clear_cart(self):
        self.items.clear()
