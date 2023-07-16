# Anh Vo
# 2037824
# Lab 10.19

# Represents an item to be purchased
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        # Initialize ItemToPurchase object with provided or default values
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        # Prints the cost of the item based on quantity and price
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')

    def print_item_description(self):
        # Prints the item's name and description
        print(f'{self.item_name}: {self.item_description}')


# Represents a shopping cart
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adds an item to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Removes an item from the cart based on its name
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print('Item not found in cart. Nothing removed.')

    # Modifies the quantity of an item in the cart based on its name
    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                item.item_quantity = modified_item.item_quantity
                return
        print('Item not found in cart. Nothing modified.')

    # Returns the total number of items in the cart
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    # Returns the total cost of the items in the cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    # Prints the shopping cart's total cost and the items in it
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f'Number of Items: {self.get_num_items_in_cart()}\n')
        total_cost = self.get_cost_of_cart()

        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
            print(f'\nTotal: ${total_cost}')

        else:
            for item in self.cart_items:
                item.print_item_cost()

            print(f'\nTotal: ${total_cost}')

    # Prints the descriptions of the items in the cart
    def print_descriptions(self):
        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print('\nItem Descriptions')

            for item in self.cart_items:
                item.print_item_description()


# Returns the menu string
def print_menu():
    return "\nMENU\n" \
           "a - Add item to cart\n" \
           "r - Remove item from cart\n" \
           "c - Change item quantity\n" \
           "i - Output items' descriptions\n" \
           "o - Output shopping cart\n" \
           "q - Quit"

# Executes the chosen menu option based on the user's choice
def execute_menu(choice, my_cart):
    if choice == 'a':
        print('\nADD ITEM TO CART')
        item_name = input("Enter the item name:\n")
        item_description = input("Enter the item description:\n")
        item_price = int(input("Enter the item price:\n"))
        item_quantity = int(input("Enter the item quantity:\n"))
        item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        my_cart.add_item(item)
        output_menu = print_menu()
        print(output_menu)

    elif choice == 'r':
        print('\nREMOVE ITEM FROM CART')
        item_name = input("Enter name of item to remove:\n")
        my_cart.remove_item(item_name)
        output_menu = print_menu()
        print(output_menu)

    elif choice == 'c':
        print('\nCHANGE ITEM QUANTITY')
        item_name = input("Enter the item name:\n")
        item_quantity = int(input("Enter the new quantity:\n"))
        modified_item = ItemToPurchase(item_name, item_quantity=item_quantity)
        my_cart.modify_item(modified_item)
        output_menu = print_menu()
        print(output_menu)

    elif choice == 'i':
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        my_cart.print_descriptions()
        output_menu = print_menu()
        print(output_menu)

    elif choice == 'o':
        print('\nOUTPUT SHOPPING CART')
        my_cart.print_total()
        output_menu = print_menu()
        print(output_menu)

    elif choice == 'q':
        return

    print()

if __name__ == "__main__":
    # Get customer's name and current date
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    # Create a new shopping cart with customer name and current date
    shopping_cart = ShoppingCart(customer_name, current_date)

    output_menu = print_menu()
    print(output_menu)
    print()
    while True:
        user_choice = input("Choose an option:")

        # Execute the chosen menu option
        execute_menu(user_choice, shopping_cart)
        if user_choice == 'q':
            print()
            break
