# Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
product = ("Laptop", 50000, "Black" ,"Samsung", "Electronics")
print(product)

# Access and print the second element of the tuple product.
sec = product[1]
print('second: ', sec)

# Slice and print the last two elements of the product tuple.
print('last two: ', product[-2:])

# Check whether "Electronics" is present in the product tuple and print a message.
print('Electronics in product: ', 'Electronics' in product)

# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
prices = (1000, 1500, 1200, 1100, 900)
print('print of 1000: ', prices.count(1000))

# Find and print the maximum and minimum price from the prices tuple.
print('max: ', max(prices))
print('min: ', min(prices))

# Use a loop to print each item from the product tuple on a new line.
for p in product:
    print(p)

# Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
prod_list = list(product)
prod_list[prod_list.index(50000)] = 55000
product = tuple(prod_list)
print(product)

# Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
product = product + ('In Stock',)
print(product)

# Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
prod_list = list(product)
prod_list.remove(('Electronics'))
product = tuple(prod_list)
print(product)

# Unpack the tuple product into three variables and print each variable.
device, price, color, company, in_stock = product
print(device, price, color, company, in_stock)

# Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.
nested_tuple = (device, (price, color), (company, in_stock))
print(nested_tuple)