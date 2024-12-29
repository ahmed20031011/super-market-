class Product:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Quantity: {self.quantity}, Price: ${self.price:.2f})"

class Customer:
    def __init__(self, customer_id, name):
        self.id = customer_id
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.quantity >= quantity:
            self.cart.append((product, quantity))
            product.quantity -= quantity
        else:
            print("Quantity is not available.")

    def view_cart(self):
        print("Cart:")
        counter = 1
        for product, quantity in self.cart:
            print(f"{counter}. {product.name}, Quantity: {quantity}")
            counter += 1

    def checkout(self, admin):
        total = sum(product.price * quantity for product, quantity in self.cart)
        print(f"Total: ${total:.2f}")
        record = f"Customer: {self.name}, Products: {[product.name for product, quantity in self.cart]}, Total: ${total:.2f}"
        admin.sales_records.append(record)
        self.cart.clear()

class Admin:
    def __init__(self):
        self.products = {}
        self.customers = {}
        self.sales_records = []

    def add_product(self, product):
        if product.id in self.products:
            print("Error: Product ID already exists.")
        else:
            self.products[product.id] = product

    def print_product_list(self):
        print("Products:")
        for product in self.products.values():
            print(product)

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity += quantity
        else:
            print("Product not found.")

    def manage_customers(self):
        print("Customers:")
        for customer in self.customers.values():
            print(customer.name)

    def view_sales_records(self):
        print("Sales Records:")
        for record in self.sales_records:
            print(record)

def main():
    admin = Admin()
    while True:
        print("\n1. Admin\n2. Customer\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            while True:
                print("\nAdmin Menu\n1. Add Product\n2. Print Product List\n3. Update Stock\n4. Manage Customers\n5. View Sales Records\n6. Back")
                admin_choice = input("Choose an option: ")
                if admin_choice == "1":
                    id = input("Enter product ID: ")
                    name = input("Enter product name: ")
                    quantity = int(input("Enter quantity: "))
                    price = float(input("Enter price: "))
                    admin.add_product(Product(id, name, quantity, price))
                elif admin_choice == "2":
                    admin.print_product_list()
                elif admin_choice == "3":
                    product_id = input("Enter product ID: ")
                    quantity = int(input("Enter quantity: "))
                    admin.update_stock(product_id, quantity)
                elif admin_choice == "4":
                    admin.manage_customers()
                elif admin_choice == "5":
                    admin.view_sales_records()
                elif admin_choice == "6":
                    break
                else:
                    print("Invalid choice. Please choose again.")
        elif choice == "2":
            customer_id = input("Enter customer ID: ")
            customer_name = input("Enter customer name: ")
            customer = Customer(customer_id, customer_name)
            admin.customers[customer_id] = customer
            while True:
                print("\nCustomer Menu\n1. Search Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Back")
                customer_choice = input("Choose an option: ")
                if customer_choice == "1":
                    search_term = input("Enter product name or ID: ")
                    for product in admin.products.values():
                        if search_term.lower() in product.name.lower() or search_term == product.id:
                            print(product)
                elif customer_choice == "2":
                    product_id = input("Enter product ID: ")
                    if product_id in admin.products:
                        quantity = int(input(f"Enter quantity of {admin.products[product_id].name.lower()} to add to cart: "))
                        customer.add_to_cart(admin.products[product_id], quantity)
                    else:
                        print("Product not found.")
                elif customer_choice == "3":
                    customer.view_cart()
                elif customer_choice == "4":
                    customer.checkout(admin)
                elif customer_choice == "5":
                    break
                else:
                    print("Invalid choice. Please choose again.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")




main()
