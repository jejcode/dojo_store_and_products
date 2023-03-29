class Product:
    all_products = []
    def __init__(self, new_product) -> None: # create instance from dictionary
        self.name = new_product['name']
        self.price = new_product['price']
        self.category = new_product['category']
        self.id = len(Product.all_products) # unique id based on number of products created
        Product.all_products.append(self) # add new_product to list in order to manage unique ids
    
    def update_price(self, percent_change, is_increased): # increases or decreases price by certain percentage
        if is_increased == True:
            self.price = self.price * percent_change + self.price
        else:
            self.price = self.price - self.price * percent_change
        return self
    
    def print_info(self): # displays class attributes
        print('-------------------------')
        print(f"Product name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: {self.price}")
        return self