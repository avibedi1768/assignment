# Problem Statement: Product Inventory Management System

# A retail store wants to digitally manage its inventory using Python.
# You are asked to design a program that allows the store to:

# Store product details

# Perform common operations like viewing, adding, updating, and calculating total inventory value

# The program should use functions, loops, lists, and tuples effectively.



# - Each product should have Name, Price, and Quantity.
# - Store this information as a tuple : (name, price, quantity).
# - Maintain a collection of products as a list of tuples.

# Example:

# products = [
#     ("Laptop", 50000, 10),
#     ("Mobile", 20000, 15),
#     ("Headphones", 1500, 25)
# ]


# (a) Function to Display Products
#    - Create a function display_products() that:
#    - Iterates over the list of products (using a loop).
#    - Prints product details (name, price, quantity).


# (b) Function to Add a New Product
#    - Create a function add_product(name, price, qty) that:
#    - Takes product details as parameters.
#    - Adds the new product (tuple) into the products list.


# (c) Function to Update Stock Quantity
#    - Create a function update_stock(product_name, new_qty) that:
#    - Loops through the products list.
#    - Finds the product by name.
#    - Updates its quantity to the new value.


# (d) Function to Calculate Total Inventory Value
#    - Create a function total_value() that:
#    - Iterates over all products.
#    - Multiplies price × quantity for each product.
#    - Returns the sum of all values.


# Create a Menu-Driven Program (Loop Requirement)

# Use a while True loop to display a menu:

# 1. Display Products
# 2. Add Product
# 3. Update Stock
# 4. Show Total Inventory Value
# 5. Exit


# Take user input for choice.

# Call the corresponding function.

# Exit when user selects option 5.

products = [
    ("Laptop", 50000, 10),
    ("Mobile", 20000, 15),
    ("Headphones", 1500, 25)
]

def display_products():
    for p in products:
        print(p)

def add_product(name, price, qty):
    products.append((name, price, qty))

def update_stock(product_name, new_qty):
    for i, p in enumerate(products):
        if p[0] == product_name:
            p_list = list(p)
            p_list[2] = new_qty
            products[i] = tuple(p_list)
            break

def total_value():
    total = 0
    
    for p in products:
        total += p[1] * p[2]
    
    return total

while True:
    a = int(input('enter your choice: '))
    
    match a:
        case 1:
            print('these are all the prods')
            display_products()
        case 2:
            print('add new product')
            name = input('enter name: ')
            price = int(input('enter price: '))
            quantity = int(input('enter quantity: '))
            
            add_product(name, price, quantity)
            
            print('now, prods:')
            display_products()
        case 3:
            print('update stock')
            name = input('enter prod name: ')
            qty = int(input('enter new quantity: '))
            
            update_stock(name, qty)
            
            print('now, prods:')
            display_products()
        case 4:
            print('total inventory value: ', total_value())
        case 5:
            print('exiting')
            break
        case default:
            print('invalid choice')