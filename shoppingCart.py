def show_menu():
    print("==== Shopping Cart ====")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")


def add_item(cart):
    item = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))

    cart.append({"item": item, "price": price, "quantity": quantity})
    print("Item added to cart!")


def remove_item(cart):
    item = input("Enter the item name to remove: ")

    for product in cart:
        if product["item"] == item:
            cart.remove(product)
            print("Item removed from cart!")
            return

    print("Item not found in cart!")


def view_cart(cart):
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    print("==== Your Cart ====")
    total = 0

    for item in cart:
        print(f"{item['item']} - ${item['price']} x {item['quantity']}")
        total += item["price"] * item["quantity"]

    print(f"Total: ${total}")


def checkout(cart):
    if len(cart) == 0:
        print("Your cart is empty. Nothing to checkout.")
        return

    print("==== Checkout ====")
    view_cart(cart)
    confirmation = input("Confirm checkout (yes/no): ")

    if confirmation.lower() == "yes":
        print("Thank you for your purchase!")
        cart.clear()
    else:
        print("Checkout canceled.")


def shopping_cart():
    cart = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            remove_item(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            print("Thank you for using the shopping cart.")
            break
        else:
            print("Invalid choice. Please try again.")


shopping_cart()
