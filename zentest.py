# Define the products and their prices
products = {"Product A": 20, "Product B": 40, "Product C": 50}

# Define the discount rules and their functions
discount_rules = {
    "flat_10_discount": lambda subtotal, quantity: 10 if subtotal > 200 else 0,
    "bulk_5_discount": lambda subtotal, quantity: sum([0.05 * products[p] * q for p, q in quantity.items() if q > 10]),
    "bulk_10_discount": lambda subtotal, quantity: 0.1 * subtotal if sum(quantity.values()) > 20 else 0,
    "tiered_50_discount": lambda subtotal, quantity: sum([0.5 * products[p] * (q - 15) for p, q in quantity.items() if sum(quantity.values()) > 30 and q > 15])
}

# Define the fees
gift_wrap_fee = 1 # per unit
shipping_fee = 5 # per package

# Ask the user for the quantity of each product and whether they want gift wrap
quantity = {} # a dictionary to store the quantity of each product
gift_wrap = {} # a dictionary to store whether the user wants gift wrap for each product
for product in products:
    print(f"How many units of {product} do you want to buy?")
    quantity[product] = int(input()) # get the user input as an integer
    print(f"Do you want gift wrap for {product}? (yes/no)")
    gift_wrap[product] = input().lower() == "yes" # get the user input as a boolean

# Calculate the subtotal
subtotal = sum([products[p] * q for p, q in quantity.items()])

# Calculate the best discount
best_discount = 0 # initialize the best discount amount to zero
best_rule = None # initialize the best discount rule to None
for rule, func in discount_rules.items():
    discount = func(subtotal, quantity) # calculate the discount amount for each rule
    if discount > best_discount: # if the discount is better than the current best discount
        best_discount = discount # update the best discount amount
        best_rule = rule # update the best discount rule

# Calculate the shipping fee
total_quantity = sum(quantity.values()) # get the total number of units
packages = (total_quantity - 1) // 10 + 1 # get the number of packages needed (round up)
shipping_fee = shipping_fee * packages # multiply by the fee per package

# Calculate the gift wrap fee
gift_wrap_fee = sum([gift_wrap[p] * q for p, q in quantity.items()]) * gift_wrap_fee # multiply by the fee per unit

# Calculate the total amount
total = subtotal - best_discount + shipping_fee + gift_wrap_fee

# Print the output details
print("\nHere are the details of your purchase:")
for product in products:
    print(f"{product}: {quantity[product]} units, ${products[product] * quantity[product]}")
print(f"Subtotal: ${subtotal}")
print(f"Discount: {best_rule}, ${best_discount}")
print(f"Shipping fee: ${shipping_fee}")
print(f"Gift wrap fee: ${gift_wrap_fee}")
print(f"Total: ${total}")



