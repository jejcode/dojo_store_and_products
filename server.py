from store import Store #import module
from product import Product # import module

new_store = Store('Best Buy') # new instance of Store
product1 = {
    'name': 'Pixel 8',
    'price': 800,
    'category': 'Phone'
}
product2 = {
    'name': 'Macbook Pro',
    'price': 2000,
    'category': 'Laptop'
}
product3 = {
    'name': 'Vizio UberWatch Experience',
    'price': 695,
    'category': 'tv'
}
new_product1 = Product(product1) # new instance of Product
new_product2 = Product(product2) # new instance of Product
new_product3 = Product(product3) # new instance of Product

# linked methods to add products to store
new_store.add_product(new_product1).add_product(new_product2).add_product(new_product3).inflation(.05)
# display info to check logic
new_product1.print_info()
new_product2.print_info()
new_product3.print_info()
new_store.set_clearance('tv',.9) # set all tvs on clearance
# display info to check logic
new_product1.print_info() 
new_product2.print_info()
new_product3.print_info()