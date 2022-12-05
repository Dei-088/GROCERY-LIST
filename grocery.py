print("="*50)
print("GROCERY LIST APP".center(50))
print("="*50)

# Loop to ask user for their budget
# Does not stop until inputted budget is numeric
while True:
    try:
        budget = float(input("Enter your budget: "))

    except ValueError:
        print("Error! Budget must be numeritc.")
        continue
    else:
        print("="*50)
        break

# Dictionary that stores each entered product
products_dict = {
    "name": [],
    "quantity": [],
    "price": []
}

# Convert dictionary to list
products_list = list(products_dict.values())

# Variables derived from the products dictionary
products_name = products_list[0]
products_quantity = products_list[1]
products_price = products_list[2]

# Loop that asks the user to pick an action
while True:
    # Print actions menu
    print("="*50)
    print("MENU".center(50))
    print("="*50)
    print("1. Add")
    print("2. Delete")
    print("3. Exit")
    print("="*50)

    # Get user input for action choice and check for errors
    try:
        choice = int(input("--> "))
        if choice not in [1,2,3]:
            print("Error! Please choose from 1-3 only.")
            continue

    except ValueError:
        print("Error! Please choose from 1-3 only.")
        continue
    else:
        print("="*50)
        # Check the selected option if budget is greater than zero 
        # Add product
        if choice == 1:
            print("Add Product".center(50))
            print("="*50)
            product_name = input("Enter product name: ")
            product_quantity = int(input("Enter quantity: "))
            product_price = float(input("Enter price of the product: "))

            if (product_price * product_quantity) > budget:
                print("Error! Product price is greater than your budget.")
                continue
            else:
                # Check if product is already in the list
                if product_name in products_name:
                    # Find prduct index
                    product_index = products_name.index(product_name)

                    # Store old price and quantity
                    old_quantity = products_quantity[product_index]
                    old_price = products_price[product_index]

                    # Add previously deducted budget
                    budget = budget + (old_price * old_quantity)

                    # Update quantity 
                    products_quantity.remove(products_quantity[product_index])

                    # Update price
                    products_price.remove(products_price[product_index])

                    # Insert new values given by the user earlier
                    products_quantity.insert(product_index, product_quantity + old_quantity)
                    products_price.insert(product_index, product_price)
                    product_quantity+=old_quantity
                else:
                    # Add all new info is product is not yet in the list
                    products_name.append(product_name)
                    products_quantity.append(product_quantity)
                    products_price.append(product_price)
                    
                # Update user budget
                budget = budget - (product_price * product_quantity)
                print(f"Your updated budget: {budget:.2f}")
                print("="*50)

        elif choice == 2:
            print("Add Product".center(50))
            print("="*50)
            # Ask user to input the name of the product to delete
            product_name = input("Enter product name: ")

            # Check if inputted product name is in grocery list
            # Initialize a counter to keep track of the product's index if it is in the list
            product_found = False 
            delete_index = -1
            ctr = 0
            for p in products_name: 
                if p.lower() == product_name.lower():
                    product_found = True
                    delete_index = ctr
                    break
                ctr+=1
            
            # If product is found in the list
            if product_found:
                # Update user's budget before deleting the product
                # Add back the previously deducted amount from their budget
                budget += (products_quantity[delete_index] * products_price[delete_index])

                # Delete product information from the grocery list
                del products_name[delete_index]
                del products_quantity[delete_index]
                del products_price[delete_index]

                # Display that deletion is successful
                print("Product has been successfully deleted!")
                print(f"Your updated budget: {budget:.2f}")
                print("="*50)
            else:
                # Display error message if product is not found in the list
                print("Error! Product cannot be found in your grocery list.")
        else:
            break


# Print the amount/budget left
print("="*50)
print(f"Amount left: {budget:.2f}")

# Print the name of the product that the user can buy with their remaining budget
if budget in products_price:
    print(f"The budget you have left can buy you a {products_name[products_price.index(budget)]}")

# Print final grocery items list
print("="*50)
print("Your final grocery list".center(50))
print("="*50)

if len(products_name) > 0:
    for i in range(len(products_name)):
        print(f"{products_name[i]}, {products_quantity[i]}x, {products_price[i]:.2f} each")
else:
    print("There are no items here...")
print("="*50)