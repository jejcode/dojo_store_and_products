class Store:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []
    
    def add_product(self, new_product): # add product to store list
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        for i in range(0,len(self.products)): # iterate list and find index of product.id
            if self.products[i].id == id: #find matching product
                print(vars(self.products.pop(i))) # removes product AND prints it's key,value pairs
        return self
    
    def inflation(self, perc): # adjust prices to inflation rate
        for product in self.products:
            product.price = product.price * perc + product.price
        return self
    
    def set_clearance(self, category, percent_discount): # set clearance for a category
        for product in self.products:
            if product.category == 'tv':
                product.update_price(percent_discount,False) # use the Product class method to adjust price
        return self
