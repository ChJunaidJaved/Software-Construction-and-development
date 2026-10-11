class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def remove_item(self, name):
        for item in self.items:
            if item["name"].lower() == name.lower():
                self.items.remove(item)
                return True

        return False

    def display_cart(self):
        print("\nShopping Cart:")

        for item in self.items:
            subtotal = item["price"] * item["quantity"]
            print(
                f'{item["name"]} - '
                f'Price: Rs. {item["price"]}, '
                f'Quantity: {item["quantity"]}, '
                f'Subtotal: Rs. {subtotal}'
            )

        print(f"Total: Rs. {self.calculate_total()}")


cart1 = ShoppingCart()
cart1.add_item("Laptop", 75000, 1)
cart1.add_item("Mouse", 800, 2)

cart2 = ShoppingCart()
cart2.add_item("Keyboard", 3550, 1)
cart2.add_item("Headphones", 3000, 2)

cart1.display_cart()
cart2.display_cart()

